param(
  [string]$IdentityPath = "examples/governance/identity-claim.sample.json",
  [string]$CapabilityPath = "examples/governance/capability-declaration.sample.json"
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

function Test-NonEmptyArray {
  param(
    [System.Collections.Generic.List[string]]$Errors,
    [object]$Value,
    [string]$Path
  )

  if ($null -eq $Value -or -not ($Value -is [System.Array]) -or $Value.Count -lt 1) {
    Add-Error $Errors "$Path must be a non-empty array"
  }
}

$errors = [System.Collections.Generic.List[string]]::new()

$identity = Read-JsonFile $IdentityPath
$capability = Read-JsonFile $CapabilityPath

Test-Required $errors $identity @("subject_id", "subject_type", "display_name", "issuer", "issued_at", "responsibility_owner", "audit_required") "identityClaim"
Test-Enum $errors $identity.subject_type @("human", "ai_agent", "organization", "platform", "guardian_node", "state_institution", "composite_subject", "other") "identityClaim.subject_type"
Test-Enum $errors $identity.trust_level @("unknown", "self_claimed", "issuer_verified", "guardian_verified", "institution_verified") "identityClaim.trust_level"

Test-Required $errors $capability @("subject_id", "capabilities", "prohibited_actions", "risk_level", "requires_human_review", "fallback_mode") "capabilityDeclaration"
Test-NonEmptyArray $errors $capability.capabilities "capabilityDeclaration.capabilities"
Test-Enum $errors $capability.risk_level @("low", "medium", "high", "critical") "capabilityDeclaration.risk_level"
Test-Enum $errors $capability.human_review_threshold @("none", "medium", "high", "critical") "capabilityDeclaration.human_review_threshold"
Test-Enum $errors $capability.fallback_mode @("continue_with_logging", "downgrade", "pause", "human_handoff", "circuit_break") "capabilityDeclaration.fallback_mode"

if ($identity.subject_id -ne $capability.subject_id) {
  Add-Error $errors "capabilityDeclaration.subject_id must match identityClaim.subject_id"
}

if ($identity.metadata.certification_claim -and $identity.metadata.certification_claim -ne "none") {
  Add-Error $errors "sample identityClaim.metadata.certification_claim should be none"
}

if ($capability.can_execute_actions -ne $false) {
  Add-Error $errors "sample capabilityDeclaration.can_execute_actions should be false"
}

if ($capability.can_make_promises -ne $false) {
  Add-Error $errors "sample capabilityDeclaration.can_make_promises should be false"
}

if ($errors.Count -gt 0) {
  Write-Host "Node contract validation failed:" -ForegroundColor Red
  foreach ($error in $errors) {
    Write-Host " - $error" -ForegroundColor Red
  }
  exit 1
}

Write-Output "Node contract validation OK"
Write-Output "Validated chain:"
Write-Output "  $IdentityPath"
Write-Output "  -> $CapabilityPath"


