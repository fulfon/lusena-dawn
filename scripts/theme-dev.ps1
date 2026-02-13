param(
  [string]$ConfigPath = "config/shopify.theme.tom.txt",
  [string]$Store,
  [string]$StorePassword,
  [string]$ListenHost,
  [int]$Port
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Get-ConfigValue {
  param(
    [string]$Content,
    [string]$Key
  )

  $escapedKey = [regex]::Escape($Key)
  $pattern = "(?im)^\s*$escapedKey\s*=\s*`"([^`"]*)`"\s*$"
  $match = [regex]::Match($Content, $pattern)
  if ($match.Success) { return $match.Groups[1].Value }
  return $null
}

$resolvedConfigPath = Resolve-Path -LiteralPath $ConfigPath -ErrorAction SilentlyContinue
if (-not $resolvedConfigPath) {
  throw "Config file not found: $ConfigPath"
}

$configContent = Get-Content -LiteralPath $resolvedConfigPath -Raw

if (-not $Store) { $Store = Get-ConfigValue -Content $configContent -Key "store" }
if (-not $StorePassword) { $StorePassword = Get-ConfigValue -Content $configContent -Key "store_password" }
if (-not $ListenHost) { $ListenHost = (Get-ConfigValue -Content $configContent -Key "host") }
if (-not $Port) {
  $portText = Get-ConfigValue -Content $configContent -Key "port"
  if ($portText -match "^\d+$") { $Port = [int]$portText }
}

if (-not $Store) { throw "Missing 'store' in $ConfigPath" }
if (-not $StorePassword) { throw "Missing 'store_password' in $ConfigPath" }
if (-not $ListenHost) { $ListenHost = "127.0.0.1" }
if (-not $Port) { $Port = 9292 }

$args = @(
  "theme",
  "dev",
  "--store", $Store,
  "--store-password", $StorePassword,
  "--host", $ListenHost,
  "--port", "$Port"
)

Write-Host "Starting Shopify theme dev on http://$ListenHost`:$Port (store: $Store)"
& shopify @args
