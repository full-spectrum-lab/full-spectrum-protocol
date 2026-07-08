$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$markdownFiles = Get-ChildItem -Path $repoRoot -Recurse -File -Include *.md |
  Where-Object {
    $_.FullName -notmatch "\\.git\\" -and
    $_.FullName -notmatch "\\node_modules\\"
  }

$failures = New-Object System.Collections.Generic.List[string]

foreach ($file in $markdownFiles) {
  $text = Get-Content -LiteralPath $file.FullName -Raw
  $matches = [regex]::Matches($text, '(?<!\!)\[[^\]]+\]\(([^)]+)\)|!\[[^\]]*\]\(([^)]+)\)')

  foreach ($match in $matches) {
    $rawTarget = if ($match.Groups[1].Success) { $match.Groups[1].Value } else { $match.Groups[2].Value }
    $target = $rawTarget.Trim()

    if ([string]::IsNullOrWhiteSpace($target)) { continue }
    if ($target.StartsWith("#")) { continue }
    if ($target -match "^(https?|mailto|tel|data):") { continue }

    # Strip optional Markdown title: [label](path "title")
    if ($target.StartsWith("<") -and $target.Contains(">")) {
      $target = $target.Substring(1, $target.IndexOf(">") - 1)
    } elseif ($target -match '^(?<path>[^\s]+)\s+["'']') {
      $target = $Matches["path"]
    }

    # Strip anchor/query for local path existence checks.
    $target = ($target -split "#", 2)[0]
    $target = ($target -split "\?", 2)[0]
    if ([string]::IsNullOrWhiteSpace($target)) { continue }

    try {
      $target = [System.Uri]::UnescapeDataString($target)
    } catch {
      # Keep original target if URL decoding fails.
    }

    $baseDir = Split-Path -Parent $file.FullName
    $resolved = Join-Path $baseDir $target

    if (-not (Test-Path -LiteralPath $resolved)) {
      $relativeFile = Resolve-Path -LiteralPath $file.FullName -Relative
      $failures.Add("${relativeFile}: missing local link '$rawTarget'")
    }
  }
}

if ($failures.Count -gt 0) {
  Write-Host "Broken local documentation links detected:" -ForegroundColor Red
  $failures | ForEach-Object { Write-Host " - $_" -ForegroundColor Red }
  exit 1
}

Write-Host "Documentation local links OK: checked $($markdownFiles.Count) Markdown files."

