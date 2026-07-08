param(
  [string]$SamplePath = "examples/governance/governance-event.sample.json"
)

$ErrorActionPreference = "Stop"

$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
Set-Location $RepoRoot

function Read-JsonFile {
  param(
    [Parameter(Mandatory = $true)][string]$Path
  )

  if (-not (Test-Path -LiteralPath $Path)) {
    throw "File not found: $Path"
  }

  try {
    return Get-Content -LiteralPath $Path -Raw -Encoding UTF8 | ConvertFrom-Json
  } catch {
    throw "Invalid JSON: $Path. $($_.Exception.Message)"
  }
}

function Add-Error {
  param(
    [System.Collections.Generic.List[string]]$Errors,
    [string]$Message
  )
  $Errors.Add($Message) | Out-Null
}

function Test-Required {
  param(
    [System.Collections.Generic.List[string]]$Errors,
    [object]$Object,
    [string[]]$Fields,
    [string]$Prefix
  )

  $names = @($Object.PSObject.Properties.Name)
  foreach ($field in $Fields) {
    if (-not ($names -contains $field)) {
      Add-Error $Errors "$Prefix missing required field: $field"
    }
  }
}

function Test-Enum {
  param(
    [System.Collections.Generic.List[string]]$Errors,
    [object]$Value,
    [object[]]$Allowed,
    [string]$Path
  )

  if ($null -eq $Value) {
    return
  }

  if (-not ($Allowed -contains $Value)) {
    Add-Error $Errors "$Path has invalid enum value '$Value'. Allowed: $($Allowed -join ', ')"
  }
}

$errors = [System.Collections.Generic.List[string]]::new()
$sample = Read-JsonFile $SamplePath

Test-Required $errors $sample @("event_id", "event_type", "actor", "action", "context") "governanceEvent"
Test-Enum $errors $sample.event_type @("ai_action", "tool_call", "recommendation", "commitment", "refusal", "escalation", "review") "governanceEvent.event_type"

Test-Required $errors $sample.actor @("type", "id") "governanceEvent.actor"
Test-Enum $errors $sample.actor.type @("human", "ai_agent", "system", "organization", "network") "governanceEvent.actor.type"

Test-Required $errors $sample.action @("type", "description") "governanceEvent.action"
Test-Required $errors $sample.context @("domain", "data_mode") "governanceEvent.context"
Test-Enum $errors $sample.context.data_mode @("synthetic", "desensitized", "private_internal", "public") "governanceEvent.context.data_mode"

if ($sample.declared_boundary -and $sample.declared_boundary.may_execute_enterprise_action -ne $false) {
  Add-Error $errors "governanceEvent.declared_boundary.may_execute_enterprise_action should be false for this non-invasive synthetic sample"
}

Test-Enum $errors $sample.review_requirement @("none", "recommended", "human_review_required", "organizational_review_required", "external_review_required") "governanceEvent.review_requirement"

if ($errors.Count -gt 0) {
  Write-Host "GovernanceEvent validation failed:" -ForegroundColor Red
  foreach ($error in $errors) {
    Write-Host " - $error" -ForegroundColor Red
  }
  exit 1
}

Write-Output "GovernanceEvent validation OK"
Write-Output "Validated sample:"
Write-Output "  $SamplePath"

