Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Parse-TomlString {
  param([Parameter(Mandatory = $true)][string]$Value)

  $v = $Value.Trim()
  if ($v.Length -lt 2) { return $v }

  $q = $v[0]
  if (($q -ne '"') -and ($q -ne "'")) { return $v }
  if ($v[$v.Length - 1] -ne $q) { return $v }

  $inner = $v.Substring(1, $v.Length - 2)
  if ($q -eq '"') {
    $inner = $inner.Replace('\"', '"').Replace('\\', '\')
  }
  return $inner
}

function Split-TomlArrayItems {
  param([Parameter(Mandatory = $true)][string]$Inner)

  $items = New-Object System.Collections.Generic.List[string]
  $sb = New-Object System.Text.StringBuilder
  $quote = [char]0
  $escape = $false

  foreach ($c in $Inner.ToCharArray()) {
    if ($escape) {
      [void]$sb.Append($c)
      $escape = $false
      continue
    }

    if ($quote -ne [char]0) {
      if ($quote -eq '"' -and $c -eq '\') {
        $escape = $true
        [void]$sb.Append($c)
        continue
      }
      if ($c -eq $quote) {
        $quote = [char]0
      }
      [void]$sb.Append($c)
      continue
    }

    if ($c -eq '"' -or $c -eq "'") {
      $quote = $c
      [void]$sb.Append($c)
      continue
    }

    if ($c -eq ',') {
      $items.Add($sb.ToString().Trim())
      [void]$sb.Clear()
      continue
    }

    [void]$sb.Append($c)
  }

  $tail = $sb.ToString().Trim()
  if ($tail -ne '') {
    $items.Add($tail)
  }

  return ,$items.ToArray()
}

function Parse-TomlValue {
  param([Parameter(Mandatory = $true)][string]$Value)

  $v = $Value.Trim()
  if ($v -match '^(true|false)$') { return [bool]::Parse($v) }

  if ($v -match '^-?\d+(\.\d+)?$') {
    $n = 0.0
    if ([double]::TryParse($v, [ref]$n)) { return $n }
  }

  if ($v.StartsWith('[') -and $v.EndsWith(']')) {
    $inner = $v.Substring(1, $v.Length - 2).Trim()
    if ($inner -eq '') { return @() }
    $rawItems = Split-TomlArrayItems -Inner $inner
    return @($rawItems | ForEach-Object { Parse-TomlValue -Value $_ })
  }

  if ($v.StartsWith('"') -or $v.StartsWith("'")) {
    return Parse-TomlString -Value $v
  }

  return $v
}

function Get-CodexMcpServersFromToml {
  param([Parameter(Mandatory = $true)][string]$TomlPath)

  $servers = @{}
  $currentServer = $null
  $currentSub = $null # root | env | http_headers | env_http_headers | headers

  foreach ($rawLine in (Get-Content -LiteralPath $TomlPath)) {
    $line = $rawLine.Trim()
    if ($line -eq '' -or $line.StartsWith('#')) { continue }

    if ($line -match '^\[(.+)\]$') {
      $section = $Matches[1].Trim()

      if ($section -match '^mcp_servers\.([^.]+)$') {
        $currentServer = $Matches[1]
        $currentSub = 'root'
        if (-not $servers.ContainsKey($currentServer)) { $servers[$currentServer] = @{} }
        continue
      }

      if ($section -match '^mcp_servers\.([^.]+)\.env$') {
        $currentServer = $Matches[1]
        $currentSub = 'env'
        if (-not $servers.ContainsKey($currentServer)) { $servers[$currentServer] = @{} }
        if (-not $servers[$currentServer].ContainsKey('env')) { $servers[$currentServer]['env'] = @{} }
        continue
      }

      if ($section -match '^mcp_servers\.([^.]+)\.(http_headers|headers|env_http_headers)$') {
        $currentServer = $Matches[1]
        $currentSub = $Matches[2]
        if (-not $servers.ContainsKey($currentServer)) { $servers[$currentServer] = @{} }
        if (-not $servers[$currentServer].ContainsKey($currentSub)) { $servers[$currentServer][$currentSub] = @{} }
        continue
      }

      $currentServer = $null
      $currentSub = $null
      continue
    }

    if (-not $currentServer) { continue }
    if ($line -notmatch '^(?<key>[A-Za-z0-9_\-]+)\s*=\s*(?<value>.+)$') { continue }

    $key = $Matches['key']
    $value = Parse-TomlValue -Value $Matches['value']

    if ($currentSub -eq 'env' -or $currentSub -eq 'http_headers' -or $currentSub -eq 'headers' -or $currentSub -eq 'env_http_headers') {
      if (-not $servers[$currentServer].ContainsKey($currentSub)) { $servers[$currentServer][$currentSub] = @{} }
      $servers[$currentServer][$currentSub][$key] = $value
      continue
    }

    $servers[$currentServer][$key] = $value
  }

  return $servers
}

function ConvertTo-HashtableDeep {
  param([Parameter(Mandatory = $true)]$InputObject)

  if ($null -eq $InputObject) { return $null }

  if ($InputObject -is [System.Collections.IDictionary]) {
    $h = @{}
    foreach ($k in $InputObject.Keys) {
      $h[$k] = ConvertTo-HashtableDeep -InputObject $InputObject[$k]
    }
    return $h
  }

  if ($InputObject -is [System.Collections.IEnumerable] -and -not ($InputObject -is [string])) {
    $arr = @()
    foreach ($item in $InputObject) {
      $arr += ,(ConvertTo-HashtableDeep -InputObject $item)
    }
    return $arr
  }

  if ($InputObject -is [pscustomobject]) {
    $h = @{}
    foreach ($p in $InputObject.PSObject.Properties) {
      $h[$p.Name] = ConvertTo-HashtableDeep -InputObject $p.Value
    }
    return $h
  }

  return $InputObject
}

function Write-JsonFileNoBom {
  param(
    [Parameter(Mandatory = $true)][string]$Path,
    [Parameter(Mandatory = $true)][string]$Json
  )

  $dir = Split-Path -Parent $Path
  if ($dir -and -not (Test-Path -LiteralPath $dir)) {
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
  }

  $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
  [System.IO.File]::WriteAllText($Path, $Json + "`n", $utf8NoBom)
}

function New-OpenCodeLocalCommandWithOptionalCwd {
  param(
    [Parameter(Mandatory = $true)][string]$Command,
    [Parameter()][object[]]$Args,
    [Parameter()][string]$Cwd
  )

  $argList = @()
  if ($Args) { $argList = @($Args | ForEach-Object { [string]$_ }) }

  if (-not $Cwd) {
    return ,(@([string]$Command) + $argList)
  }

  $cmdLine = @()
  $cmdLine += "cd /d ""$Cwd"""
  $cmdLine += "&&"
  $cmdLine += ("""$Command""")
  foreach ($a in $argList) {
    if ($a -match '\s' -and -not ($a.StartsWith('"') -and $a.EndsWith('"'))) {
      $cmdLine += ("""$a""")
    }
    else {
      $cmdLine += $a
    }
  }

  return @('cmd', '/c', ($cmdLine -join ' '))
}

$repoRoot = (Resolve-Path -LiteralPath '.').Path
$userProfile = [Environment]::GetFolderPath('UserProfile')
$codexConfigPath = Join-Path -Path $userProfile -ChildPath '.codex\config.toml'
$opencodeConfigPath = Join-Path -Path $repoRoot -ChildPath 'opencode.json'

if (-not (Test-Path -LiteralPath $codexConfigPath)) {
  throw "Codex config not found: $codexConfigPath"
}

$codexServers = Get-CodexMcpServersFromToml -TomlPath $codexConfigPath
if ($codexServers.Keys.Count -eq 0) {
  throw "No [mcp_servers.*] entries found in $codexConfigPath"
}

$existing = @{}
if (Test-Path -LiteralPath $opencodeConfigPath) {
  $raw = Get-Content -LiteralPath $opencodeConfigPath -Raw -ErrorAction SilentlyContinue
  if ($null -ne $raw -and $raw.Trim() -ne '') {
    $existing = ConvertTo-HashtableDeep -InputObject (ConvertFrom-Json -InputObject $raw)
  }
}

if (-not $existing.ContainsKey('$schema')) { $existing['$schema'] = 'https://opencode.ai/config.json' }
if (-not $existing.ContainsKey('mcp')) { $existing['mcp'] = @{} }

foreach ($name in ($codexServers.Keys | Sort-Object)) {
  $src = $codexServers[$name]

  if ($src.ContainsKey('command')) {
    $timeoutMs = $null
    if ($src.ContainsKey('tool_timeout_sec')) { $timeoutMs = [int]([double]$src['tool_timeout_sec'] * 1000) }

    $cmd = New-OpenCodeLocalCommandWithOptionalCwd -Command ([string]$src['command']) -Args ($src['args']) -Cwd ($src['cwd'])
    $entry = [ordered]@{
      type = 'local'
      command = $cmd
      enabled = $true
    }

    if ($src.ContainsKey('env') -and $src['env'].Count -gt 0) {
      $entry['environment'] = $src['env']
    }

    if ($null -ne $timeoutMs -and $timeoutMs -gt 0) {
      $entry['timeout'] = $timeoutMs
    }

    $existing['mcp'][$name] = $entry
    continue
  }

  if ($src.ContainsKey('url')) {
    $timeoutMs = $null
    if ($src.ContainsKey('tool_timeout_sec')) { $timeoutMs = [int]([double]$src['tool_timeout_sec'] * 1000) }

    $headers = @{}
    if ($src.ContainsKey('http_headers')) {
      foreach ($k in $src['http_headers'].Keys) { $headers[$k] = [string]$src['http_headers'][$k] }
    }
    if ($src.ContainsKey('headers')) {
      foreach ($k in $src['headers'].Keys) { $headers[$k] = [string]$src['headers'][$k] }
    }
    if ($src.ContainsKey('env_http_headers')) {
      foreach ($k in $src['env_http_headers'].Keys) { $headers[$k] = ("{env:" + [string]$src['env_http_headers'][$k] + "}") }
    }
    if ($src.ContainsKey('bearer_token_env_var')) {
      $headers['Authorization'] = ("Bearer {env:" + [string]$src['bearer_token_env_var'] + "}")
    }

    $entry = [ordered]@{
      type = 'remote'
      url = [string]$src['url']
      enabled = $true
    }

    if ($headers.Count -gt 0) { $entry['headers'] = $headers }
    if ($src.ContainsKey('bearer_token_env_var')) { $entry['oauth'] = $false }
    if ($src.ContainsKey('env') -and $src['env'].Count -gt 0) { $entry['environment'] = $src['env'] }
    if ($null -ne $timeoutMs -and $timeoutMs -gt 0) { $entry['timeout'] = $timeoutMs }

    $existing['mcp'][$name] = $entry
    continue
  }
}

$json = ($existing | ConvertTo-Json -Depth 30)
Write-JsonFileNoBom -Path $opencodeConfigPath -Json $json

Write-Output "Updated OpenCode config: $opencodeConfigPath"
