param(
  [string]$Path = "."
)

$ErrorActionPreference = "Stop"

function New-StringFromCodePoints {
  param([int[]]$CodePoints)
  $builder = New-Object System.Text.StringBuilder
  foreach ($codePoint in $CodePoints) {
    [void]$builder.Append([char]$codePoint)
  }
  $builder.ToString()
}

# Keep this script ASCII-only so Windows PowerShell 5.1 can parse it reliably.
# Typical mojibake fingerprints generated when UTF-8 Chinese text is read as GBK/ANSI:
# - "ni shuo" style mojibake: U+6D63 U+72BA
# - "full spectrum" style mojibake fragments: U+934F U+3129, U+68F0 U+6223, U+748B
# - smart quote mojibake: U+9225
# - common UTF-8-as-GBK fragments in Chinese examples: U+93B4, U+93C8, U+93C7, U+9365, U+6A83, U+3135
# - replacement character: U+FFFD
$patterns = @(
  (New-StringFromCodePoints @(0x6D63, 0x72BA)),
  (New-StringFromCodePoints @(0x934F, 0x3129)),
  (New-StringFromCodePoints @(0x68F0, 0x6223)),
  (New-StringFromCodePoints @(0x748B)),
  (New-StringFromCodePoints @(0x9225)),
  (New-StringFromCodePoints @(0x93B4)),
  (New-StringFromCodePoints @(0x93C8)),
  (New-StringFromCodePoints @(0x93C7)),
  (New-StringFromCodePoints @(0x9365)),
  (New-StringFromCodePoints @(0x6A83)),
  (New-StringFromCodePoints @(0x3135)),
  ([string][char]0x00C3),
  ([string][char]0x00C2),
  ([string][char]0xFFFD)
)

$extensions = @("*.md", "*.txt", "*.json", "*.yml", "*.yaml", "*.ts", "*.js", "*.html", "*.css")
$files = foreach ($ext in $extensions) {
  Get-ChildItem -LiteralPath $Path -Recurse -File -Filter $ext -ErrorAction SilentlyContinue |
    Where-Object { $_.FullName -notmatch "\\.git\\" }
}

$hits = @()

foreach ($file in $files) {
  $text = [System.Text.Encoding]::UTF8.GetString([System.IO.File]::ReadAllBytes($file.FullName))
  foreach ($pattern in $patterns) {
    if ($text.Contains($pattern)) {
      $hits += [pscustomobject]@{
        File = $file.FullName
        PatternCodePoints = (($pattern.ToCharArray() | ForEach-Object { ("U+{0:X4}" -f [int]$_) }) -join " ")
      }
    }
  }
}

if ($hits.Count -gt 0) {
  Write-Host "Potential mojibake detected:" -ForegroundColor Red
  $hits | Format-Table -AutoSize
  exit 1
}

Write-Host "No common mojibake patterns detected." -ForegroundColor Green

