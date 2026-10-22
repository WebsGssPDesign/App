# Parche: iniciar.ps1

## 1. Parametros

```powershell
param(
  [switch]$NoCargarModelos,
  [switch]$Recargar,          # NUEVO: unico caso en que se desmonta algo
  [int]$Ctx = 8192            # BAJADO de 25000 a 8192
)
```

## 2. Modelos-Cargados y Load-Seguro

```powershell
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
```

## 3. Cargar-Modelos

```powershell
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
```

## 4. Probar-Modelos

En el cuerpo del POST de chat:

```powershell
$cuerpo = @{
  model = $Chat
  messages = @(@{ role = "user"; content = "Responde solo: ok" })
  max_tokens = 8
  temperature = 0
  chat_template_kwargs = @{ enable_thinking = $false }
} | ConvertTo-Json -Depth 6
```

## 5. Pasar el modelo a los tres pasos

```powershell
Paso "Aprender documentos" "aprender.py" @("--model", $Chat)
Paso "Crear skills"        "crear_skills.py" @("--model", $Chat)
Paso "Aprender web"        "aprender_web.py" @("--model", $Chat)
```

## 6. Heartbeat, STOP_INDEXER y exit code

Antes de lanzar el indexador:

```powershell
Remove-Item (Join-Path $Aqui ".memoria\STOP_INDEXER") -Force -ErrorAction SilentlyContinue
```

Funcion de latido:

```powershell
$hb = Join-Path $Aqui "..\Sistema\heartbeat.json"
function Latir($paso) {
  New-Item -ItemType Directory -Force -Path (Split-Path $hb) | Out-Null
  $json = @{ estado="activo"; paso=$paso; pid=$PID; actualizado=(Get-Date -Format "yyyy-MM-dd HH:mm:ss") } | ConvertTo-Json
  [IO.File]::WriteAllText($hb, $json)
}
```

Cuenta los fallos y termina con:

```powershell
if ($fallos -gt 0) { exit 2 } else { exit 0 }
```

## 7. Transcript condicionado

```powershell
try { Start-Transcript -Path $Log -Append | Out-Null; $script:transcriptOk = $true }
catch { $script:transcriptOk = $false }
# ...
if ($script:transcriptOk) { Stop-Transcript | Out-Null }
```

## 8. Rotacion de log

Al arrancar: si `pipeline.log` supera 5 MB, renombralo a `pipeline.1.log`.
