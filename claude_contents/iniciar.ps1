# iniciar.ps1
# Ejecuta el pipeline de aprendizaje con reintentos y deja un registro en  <boveda>\.memoria\pipeline.log
#   - indexer.py --watch en segundo plano durante todo el proceso (vectoriza documentos y codigo
#     a medida que aprende; cada nota nueva ademas se indexa al instante)
#   1) aprender.py     (resume tus documentos)
#   2) crear_skills.py (crea skills en borrador a partir de lo aprendido; se omite con -SinSkills)
#   3) aprender_web.py (solo con -Web; corre sin fin)
#   4) una indexacion final al terminar
# Si un paso se corta, lo reintenta solo (hasta 6 veces).
#
# MODELOS: por defecto este script recarga los modelos en LM Studio (lms unload --all + lms load).
# Eso DESCARGA el modelo que usa OrderCode: usalo solo desde tu propia ventana de PowerShell.
# Si lo lanza el agente de OrderCode, usa SIEMPRE -NoCargarModelos (no toca los modelos cargados).
#
# Uso:
#   powershell -ExecutionPolicy Bypass -File .\iniciar.ps1                       (recarga modelos y corre)
#   powershell -ExecutionPolicy Bypass -File .\iniciar.ps1 -NoCargarModelos -Web  (desde OrderCode)
#   powershell -ExecutionPolicy Bypass -File .\iniciar.ps1 -SoloModelos           (solo recarga modelos)
# Para detener con calma: crea el archivo vacio  <boveda>\.memoria\STOP
# Nombres exactos de modelos:  lms ls   (pasalos con -Chat y -Emb si hace falta).
# (Este script no se ha podido probar en tu equipo: si algo falla, copia el mensaje y revisalo.)
param(
    [string]$Chat = "qwen3.5-9b",
    [string]$Emb  = "text-embedding-qwen3-embedding-0.6b",
    [int]$Ctx     = 25000,
    [switch]$NoCargarModelos,
    [switch]$SoloModelos,
    [switch]$SinAprender,
    [switch]$SinSkills,
    [switch]$SinIndexarAlMismoTiempo,
    [switch]$Web
)

$Aqui = $PSScriptRoot
$Py   = Join-Path $Aqui ".venv\Scripts\python.exe"
$Api  = "http://127.0.0.1:1234/v1"
$Boveda = $env:MEMORIA_VAULT
if (-not $Boveda) { $Boveda = "F:\automatizaciones\homeLab" }
$Mem  = Join-Path $Boveda ".memoria"
$Stop = Join-Path $Mem "STOP"
$Log  = Join-Path $Mem "pipeline.log"
$env:PYTHONIOENCODING = "utf-8"

New-Item -ItemType Directory -Force $Mem | Out-Null
try { Start-Transcript -Path $Log -Append | Out-Null } catch { }

$Lms = $null
$cmd = Get-Command lms -ErrorAction SilentlyContinue
if ($cmd) { $Lms = $cmd.Source }
if (-not $Lms) { $Lms = Join-Path $env:USERPROFILE ".lmstudio\bin\lms.exe" }
if (-not $NoCargarModelos -and -not (Test-Path $Lms)) {
    Write-Host "No encuentro el comando lms de LM Studio: $Lms  (o usa -NoCargarModelos)"
    exit 1
}
if (-not (Test-Path $Py)) {
    Write-Host "No encuentro el entorno de Python: $Py (crea el .venv como indica el README)"
    exit 1
}

function Servidor-Activo {
    try { Invoke-RestMethod "$Api/models" -TimeoutSec 5 | Out-Null; return $true } catch { return $false }
}

function Asegurar-Servidor {
    if (Servidor-Activo) { return $true }
    if ($NoCargarModelos) {
        Write-Host "El servidor de LM Studio no responde y no puedo iniciarlo en este modo."
        return $false
    }
    Write-Host "El servidor de LM Studio no responde. Intento iniciarlo..."
    & $Lms server start | Out-Null
    for ($i = 0; $i -lt 30; $i++) {
        Start-Sleep 2
        if (Servidor-Activo) { return $true }
    }
    Write-Host "No se pudo iniciar el servidor. Inicialo a mano en LM Studio (pestana Developer -> Start Server)."
    return $false
}

# Una peticion minima a cada modelo para confirmar que responden de verdad.
function Probar-Modelos {
    try {
        $body = @{ model = $Chat; messages = @(@{ role = "user"; content = "Responde: ok" }); max_tokens = 5 } | ConvertTo-Json -Depth 5
        Invoke-RestMethod "$Api/chat/completions" -Method Post -ContentType "application/json" -Body $body -TimeoutSec 240 | Out-Null
        $b2 = @{ model = $Emb; input = "prueba" } | ConvertTo-Json
        Invoke-RestMethod "$Api/embeddings" -Method Post -ContentType "application/json" -Body $b2 -TimeoutSec 60 | Out-Null
        return $true
    } catch {
        Write-Host "Los modelos no responden: $_"
        return $false
    }
}

function Cargar-Modelos {
    if (-not (Asegurar-Servidor)) { return $false }
    if ($NoCargarModelos) {
        # No se toca nada: solo se comprueba que lo que ya esta cargado responde.
        return (Probar-Modelos)
    }
    Write-Host "Descargando modelos cargados y cargando de nuevo (contexto $Ctx)..."
    & $Lms unload --all | Out-Null

    & $Lms load $Emb --gpu max --identifier $Emb
    if ($LASTEXITCODE -ne 0) {
        Write-Host "No pude cargar el modelo de embeddings '$Emb'. Mira los nombres con: lms ls"
        return $false
    }
    & $Lms load $Chat --gpu max --context-length $Ctx --identifier $Chat
    if ($LASTEXITCODE -ne 0) {
        Write-Host "No pude cargar el modelo de chat '$Chat'. Mira los nombres con: lms ls  (o prueba con un -Ctx menor)"
        return $false
    }
    if (-not (Probar-Modelos)) { return $false }
    Write-Host "Modelos listos."
    return $true
}

function Paso($nombre, $script, $argumentos) {
    for ($i = 1; $i -le 6; $i++) {
        if (Test-Path $Stop) { Write-Host "Archivo STOP detectado: no ejecuto '$nombre'."; return $false }
        Write-Host ""
        Write-Host "=== $nombre (intento $i de 6) $(Get-Date -Format 'HH:mm:ss') ==="
        & $Py (Join-Path $Aqui $script) @argumentos
        if ($LASTEXITCODE -eq 0) { return $true }
        if (Test-Path $Stop) { return $false }
        Write-Host "$nombre termino con codigo $LASTEXITCODE. Espero 30 s, reviso los modelos y reintento."
        Start-Sleep 30
        if (-not (Cargar-Modelos)) { Start-Sleep 60 }
    }
    Write-Host "$nombre no se pudo completar tras 6 intentos. Revisa LM Studio y vuelve a lanzar este script: retoma donde quedo."
    return $false
}

Set-Location $Aqui
Remove-Item $Stop -Force -ErrorAction SilentlyContinue   # un STOP viejo no debe impedir arrancar

$listo = $false
for ($i = 1; $i -le 3 -and -not $listo; $i++) {
    $listo = Cargar-Modelos
    if (-not $listo) { Start-Sleep 30 }
}
if (-not $listo) { try { Stop-Transcript | Out-Null } catch { }; exit 1 }
if ($SoloModelos) { try { Stop-Transcript | Out-Null } catch { }; exit 0 }

$bg = $null
if (-not $SinIndexarAlMismoTiempo) {
    $bg = Start-Process -FilePath $Py -ArgumentList @((Join-Path $Aqui "indexer.py"), "--watch", "60") -WorkingDirectory $Aqui -PassThru -WindowStyle Minimized
    Write-Host "Indexador en segundo plano (PID $($bg.Id))."
}

if (-not $SinAprender) { Paso "Aprender documentos" "aprender.py" @() | Out-Null }
if (-not $SinSkills -and -not (Test-Path $Stop)) { Paso "Crear skills" "crear_skills.py" @() | Out-Null }
if ($Web -and -not (Test-Path $Stop)) { Paso "Aprender web" "aprender_web.py" @() | Out-Null }

if ($bg -and -not $bg.HasExited) {
    Stop-Process -Id $bg.Id -Force -ErrorAction SilentlyContinue
    Start-Sleep 2
    # Si se corto en pleno trabajo puede quedar un bloqueo viejo: se limpia para la indexacion final.
    Remove-Item (Join-Path $Mem "sync.lock") -Force -ErrorAction SilentlyContinue
}
Remove-Item $Stop -Force -ErrorAction SilentlyContinue   # la indexacion final se hace aunque se haya pedido detener
Paso "Indexar (final)" "indexer.py" @() | Out-Null

Write-Host ""
Write-Host "Pipeline terminado $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')."
try { Stop-Transcript | Out-Null } catch { }
