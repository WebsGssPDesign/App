# -*- coding: utf-8 -*-
# iniciar.ps1 - pipeline completo: modelos -> aprender -> skills -> web -> indexar -> guardian
# Uso:   .\iniciar.ps1                     (recarga normal; no toca modelos ya cargados)
#        .\iniciar.ps1 -Recargar           (UNICO caso que desmonta algo)
#        .\iniciar.ps1 -NoCargarModelos    (salta el paso de carga)
#        .\iniciar.ps1 -Ctx 4096           (contexto del chat; por defecto 8192)
# Reconstruido segun PARCHES/iniciar.ps1.md (secciones 1-8). Termina con exit 0/2.
param(
  [switch]$NoCargarModelos,
  [switch]$Recargar,          # NUEVO: unico caso en que se desmonta algo
  [int]$Ctx = 8192            # BAJADO de 25000 a 8192
)

$ErrorActionPreference = "Continue"
$Aqui = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $Aqui

# ------------------------------------------------------------------ config
# Boveda y modelos via config.py (unica fuente de verdad; cae a DEFAULTS si
# reglas.json esta corrupto, igual que el resto del sistema).
$Pythonv = Join-Path (Split-Path $Aqui -Parent) ".venv\Scripts\python.exe"   # raiz del repo
$Python = if (Test-Path $Pythonv) { $Pythonv } elseif (Get-Command py -ErrorAction SilentlyContinue) { "py" } else { "python" }

$clavesCfg = @("rutas.boveda", "llm.modelo_chat", "llm.modelo_embed")
$cfgTxt = ""
try {
  $salidaPy = & $Python -c "import sys; sys.path.insert(0, r'$Aqui'); import config; [print(k+'='+str(config.get(k))) for k in sys.argv[1:]]" @($clavesCfg | Select-Object -Unique) 2>$null
  $cfgTxt = ($salidaPy | Out-String)
} catch { $cfgTxt = "" }
function CfgDe([string]$texto, [string]$clave) {
  if ($texto -match "(?m)^$clave\s*=\s*(.*)$") { return $Matches[1].Trim() }
  return ""
}
$Boveda = if ($env:MEMORIA_BOVEDA) { $env:MEMORIA_BOVEDA } else { CfgDe $cfgTxt "rutas.boveda" }
if (-not $Boveda) {
  # ultimo recurso: leer la ruta por defecto de config.py
  try {
    $crudo = Get-Content (Join-Path $Aqui "config.py") -Raw
    if ($crudo -match '"boveda":\s*r"([^"]+)"') { $Boveda = $Matches[1] }
  } catch {}
}
$Chat = if ($env:LLM_MODEL) { $env:LLM_MODEL } else { CfgDe $cfgTxt "llm.modelo_chat" }
$Emb  = if ($env:MEMORIA_MODELO_EMBED) { $env:MEMORIA_MODELO_EMBED } else { CfgDe $cfgTxt "llm.modelo_embed" }

$Lms = (Get-Command lms -ErrorAction SilentlyContinue).Source
if (-not $Lms) { $Lms = "lms" }

# ------------------------------------------------------------------ log + transcript (§7, §8)
$LogDir = Join-Path $Boveda "Sistema"
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
$Log = Join-Path $LogDir "pipeline.log"
if (Test-Path $Log) {                                    # rotacion: >5 MB -> pipeline.1.log
  if ((Get-Item $Log).Length -gt 5MB) {
    Move-Item $Log (Join-Path $LogDir "pipeline.1.log") -Force
  }
}
try { Start-Transcript -Path $Log -Append | Out-Null; $script:transcriptOk = $true }
catch { $script:transcriptOk = $false }

$fallos = 0

# ------------------------------------------------------------------ heartbeat (§6)
$hb = Join-Path $Aqui "..\Sistema\heartbeat.json"
function Latir($paso) {
  New-Item -ItemType Directory -Force -Path (Split-Path $hb) | Out-Null
  $json = @{ estado="activo"; paso=$paso; pid=$PID; actualizado=(Get-Date -Format "yyyy-MM-dd HH:mm:ss") } | ConvertTo-Json
  [IO.File]::WriteAllText($hb, $json)
}

# ------------------------------------------------------------------ python (resuelto arriba, en config)

# ------------------------------------------------------------------ servidor (§3 usa Asegurar-Servidor)
function Asegurar-Servidor {
  try { Invoke-RestMethod -Uri "http://127.0.0.1:1234/v1/models" -TimeoutSec 5 | Out-Null; return $true } catch {}
  Write-Host "    Servidor LM Studio caido. Intentando arrancar con 'lms server start'..."
  try { & $Lms server start 2>&1 | ForEach-Object { Write-Host "    $_" } } catch {}
  for ($i = 0; $i -lt 15; $i++) {
    Start-Sleep 2
    try { Invoke-RestMethod -Uri "http://127.0.0.1:1234/v1/models" -TimeoutSec 5 | Out-Null; return $true } catch {}
  }
  return $false
}

# ------------------------------------------------------------------ modelos (§2)
function Modelos-Cargados {
  try { return @((& $Lms ps --json 2>$null | ConvertFrom-Json) | ForEach-Object { $_.identifier }) }
  catch { return @() }
}

function Load-Seguro([string]$nombre, [string[]]$extra) {
  for ($i = 1; $i -le 3; $i++) {
    & $Lms load $nombre -y @extra 2>&1 | ForEach-Object { Write-Host "    $_" }
    if ($LASTEXITCODE -eq 0) { return $true }
    Write-Host "    load de '$nombre' fallo (codigo $LASTEXITCODE). Reintento $i/3"
    Start-Sleep 8
  }
  return $false
}

# ------------------------------------------------------------------ prueba de modelos (§4)
function Probar-Modelos {
  try {
    $cuerpo = @{
      model = $Chat
      messages = @(@{ role = "user"; content = "Responde solo: ok" })
      max_tokens = 8
      temperature = 0
      chat_template_kwargs = @{ enable_thinking = $false }
    } | ConvertTo-Json -Depth 6
    $r = Invoke-RestMethod -Uri "http://127.0.0.1:1234/v1/chat/completions" -Method Post `
         -ContentType "application/json" -Body $cuerpo -TimeoutSec 120
    $txt = ""
    if ($r.choices.Count -gt 0) { $txt = [string]$r.choices[0].message.content }
    if ($txt -match "(?i)ok") { return $true }
    Write-Host "    Prueba de chat no devolvio 'ok': '$txt'"
    return $false
  } catch {
    Write-Host "    Prueba de modelos fallo: $_"
    return $false
  }
}

function Cargar-Modelos {
  if (-not (Asegurar-Servidor)) { return $false }
  $ids = Modelos-Cargados
  if (-not $Recargar -and ($ids -contains $Chat) -and ($ids -contains $Emb)) {
    Write-Host "    Los dos modelos ya estan cargados. No se toca nada."
    return (Probar-Modelos)
  }
  if ($Recargar) {
    & $Lms unload --all -y | Out-Null
    for ($i = 0; $i -lt 20 -and (Modelos-Cargados).Count -gt 0; $i++) { Start-Sleep 2 }
  }
  if (-not (Load-Seguro $Emb @("--gpu","max"))) { return $false }
  if (-not (Load-Seguro $Chat @("--gpu","max","--context-length","$Ctx"))) { return $false }
  if (-not (Probar-Modelos)) { return $false }
  & $Lms ps | Write-Host
  return $true
}

# ------------------------------------------------------------------ pasos
function Paso([string]$nombre, [string]$script, [string[]]$extra) {
  Latir $nombre
  Write-Host "`n==> $nombre  ($script)"
  & $Python (Join-Path $Aqui $script) @extra
  if ($LASTEXITCODE -ne 0) {
    Write-Host "    FALLO: $nombre (codigo $LASTEXITCODE)" -ForegroundColor Red
    $script:fallos = $script:fallos + 1
  } else {
    Write-Host "    OK: $nombre"
  }
}

Write-Host "== Pipeline memoria_vectorial =="
Write-Host "   chat: $Chat | embed: $Emb"

if (-not $NoCargarModelos) {
  Latir "Cargar modelos"
  if (-not (Cargar-Modelos)) {
    Write-Host "FALLO: no se pudieron dejar los modelos listos. El pipeline termina." -ForegroundColor Red
    if ($script:transcriptOk) { Stop-Transcript | Out-Null }
    exit 2
  }
} else {
  Write-Host "    -NoCargarModelos: se omite la carga (el resto asume servidor operativo)."
}

# §5: pasar el modelo elegido a los tres pasos de aprendizaje
Paso "Aprender documentos" "aprender.py"      @("--model", $Chat)
Paso "Crear skills"        "crear_skills.py"  @("--model", $Chat)
Paso "Aprender web"        "aprender_web.py"  @("--model", $Chat)

# §6: borrar STOP_INDEXER antes de lanzar el indexador en segundo plano
Remove-Item (Join-Path $Aqui ".memoria\STOP_INDEXER") -Force -ErrorAction SilentlyContinue
Latir "Indexador"
$watchSeg = 20
try {
  $cfgTxtIdx = Get-Content (Join-Path $Aqui "config.py") -Raw
  if ($cfgTxtIdx -match '"watch_segundos":\s*(\d+)') { $watchSeg = [int]$Matches[1] }
} catch {}
Start-Process -FilePath $Python -ArgumentList @((Join-Path $Aqui "indexer.py"), "--watch", "$watchSeg") `
              -WorkingDirectory $Aqui -WindowStyle Hidden
Write-Host "    Indexador lanzado (watch ${watchSeg}s). Para pararlo: New-Item '.memoria\STOP_INDEXER'"

# Guardian en segundo plano (observacion; config guardian.activo en reglas.json)
Latir "Guardian"
Start-Process -FilePath $Python -ArgumentList @((Join-Path $Aqui "guardian.py")) `
              -WorkingDirectory $Aqui -WindowStyle Hidden
Write-Host "    Guardian lanzado."

Latir "Fin"
if ($fallos -gt 0) {
  Write-Host "`nPipeline terminado con $fallos paso(s) fallido(s)." -ForegroundColor Yellow
  if ($script:transcriptOk) { Stop-Transcript | Out-Null }
  exit 2
}
Write-Host "`nPipeline terminado correctamente."
if ($script:transcriptOk) { Stop-Transcript | Out-Null }
exit 0
