# Copia el contenido del paquete a la boveda, con .bak de todo lo que pise.
# Uso:  .\INSTALAR.ps1 -Simulacro   (para ver que haria)
#       .\INSTALAR.ps1              (para hacerlo)

param(
  [string]$Boveda = "F:\automatizaciones\homeLab",
  [switch]$Simulacro
)

$ErrorActionPreference = "Stop"
$origen = $PSScriptRoot
$marca  = Get-Date -Format "yyyyMMdd-HHmmss"

function Copiar($rel) {
  $desde = Join-Path $origen $rel
  $hasta = Join-Path $Boveda $rel
  if (-not (Test-Path $desde)) { return }
  $dir = Split-Path $hasta -Parent
  if (-not (Test-Path $dir)) {
    if (-not $Simulacro) { New-Item -ItemType Directory -Force -Path $dir | Out-Null }
    Write-Host "  + carpeta $dir"
  }
  if (Test-Path $hasta) {
    $bak = "$hasta.bak-$marca"
    if (-not $Simulacro) { Copy-Item $hasta $bak -Force }
    Write-Host "  ~ $rel  (.bak guardado)"
  } else {
    Write-Host "  + $rel"
  }
  if (-not $Simulacro) { Copy-Item $desde $hasta -Force }
}

Write-Host "Boveda destino: $Boveda"
if ($Simulacro) { Write-Host "(simulacro: no se escribe nada)`n" } else { Write-Host "" }

if (-not (Test-Path $Boveda)) { throw "No existe la boveda: $Boveda" }

foreach ($carpeta in @("Perfil", "Sistema")) {
  $d = Join-Path $Boveda $carpeta
  if (-not (Test-Path $d)) { New-Item -ItemType Directory -Force -Path $d | Out-Null }
}

Copiar "AGENTS.md"
Copiar "Sistema\reglas.json"
Copiar "Perfil\perfil_usuario.json"
Copiar "Perfil\intereses.json"
Copiar "Perfil\objetivos.json"

Get-ChildItem (Join-Path $origen "memoria_vectorial") -File | ForEach-Object {
  Copiar ("memoria_vectorial\" + $_.Name)
}
foreach ($sub in @("prompts", "tests", "PARCHES")) {
  $d = Join-Path $origen "memoria_vectorial\$sub"
  if (Test-Path $d) {
    Get-ChildItem $d -File | ForEach-Object {
      Copiar ("memoria_vectorial\$sub\" + $_.Name)
    }
  }
}

Write-Host "`nListo."
Write-Host "Siguiente:"
Write-Host "  1. Lee memoria_vectorial\PARCHES\00-leeme.md"
Write-Host "  2. Aplica los parches"
Write-Host "  3. cd $Boveda\memoria_vectorial"
Write-Host "  4. .\.venv\Scripts\Activate.ps1 ; python -m pytest tests -q"
