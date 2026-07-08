param(
  [string]$RequestPath = "examples/fshi/api-contract/request.sample.json",
  [string]$ResponsePath = "examples/fshi/api-contract/response.sample.json",
  [string]$RiskAlertPath = "examples/fshi/api-contract/risk-alert.sample.json",
  [string]$AuditTracePath = "examples/fshi/api-contract/audit-trace.sample.json",
  [string]$CrossEnterpriseAuditRecordPath = "examples/governance/cross-enterprise-audit-record.example.json"
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

function Test-Range {
  param(
    [System.Collections.Generic.List[string]]$Errors,
    [object]$Value,
    [double]$Min,
    [double]$Max,
    [string]$Path
  )

  if ($null -eq $Value) {
    return
  }

  if (-not ($Value -is [int] -and $Value -isnot [bool]) -and -not ($Value -is [long]) -and -not ($Value -is [double]) -and -not ($Value -is [decimal])) {
    Add-Error $Errors "$Path must be a number"
    return
  }

  if ($Value -lt $Min -or $Value -gt $Max) {
    Add-Error $Errors "$Path must be between $Min and $Max"
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

$schemas = @{
  request = Read-JsonFile "schemas/fshi-dialogue-inspection.schema.json"
  response = Read-JsonFile "schemas/fshi-dialogue-inspection-response.schema.json"
  riskAlert = Read-JsonFile "schemas/risk-alert.schema.json"
  auditTrace = Read-JsonFile "schemas/audit-trace.schema.json"
  crossEnterpriseAuditRecord = Read-JsonFile "schemas/cross-enterprise-audit-record.schema.json"
}

$request = Read-JsonFile $RequestPath
$response = Read-JsonFile $ResponsePath
$riskAlert = Read-JsonFile $RiskAlertPath
$auditTrace = Read-JsonFile $AuditTracePath
$crossEnterpriseAuditRecord = Read-JsonFile $CrossEnterpriseAuditRecordPath

# Request checks
Test-Required $errors $request @("request_id", "tenant_id", "inspection_mode", "industry_adapter", "language", "dialogue", "privacy") "request"
Test-Enum $errors $request.inspection_mode @("offline_batch", "api", "monitoring") "request.inspection_mode"
Test-Enum $errors $request.industry_adapter @("general", "logistics", "ecommerce", "finance", "insurance", "healthcare", "custom") "request.industry_adapter"
Test-Required $errors $request.dialogue @("dialogue_id", "messages") "request.dialogue"
Test-NonEmptyArray $errors $request.dialogue.messages "request.dialogue.messages"
Test-Required $errors $request.privacy @("desensitized", "contains_personal_data", "retention_policy") "request.privacy"

if ($request.execution_policy -and $request.execution_policy.fshi_may_execute_enterprise_action -ne $false) {
  Add-Error $errors "request.execution_policy.fshi_may_execute_enterprise_action must be false for the non-invasive sample"
}

# Response checks
Test-Required $errors $response @("request_id", "inspection_id", "status", "overall", "risk_items", "recommended_enterprise_actions", "protocol_objects") "response"
Test-Enum $errors $response.status @("queued", "running", "completed", "partial", "failed", "rejected") "response.status"
Test-Required $errors $response.overall @("risk_level", "requires_human_review", "summary") "response.overall"
Test-Enum $errors $response.overall.risk_level @("none", "low", "medium", "high", "critical") "response.overall.risk_level"
Test-Range $errors $response.overall.fshi_score 0 100 "response.overall.fshi_score"

foreach ($risk in @($response.risk_items)) {
  Test-Required $errors $risk @("risk_id", "dimension", "severity", "confidence", "recommended_action") "response.risk_items[]"
  Test-Enum $errors $risk.dimension @("permission_boundary", "unauthorized_promise", "state_conflict", "multi_turn_accumulation", "emotional_escalation", "privacy_or_data", "safety", "responsibility_gap", "systemic", "unknown") "response.risk_items[].dimension"
  Test-Enum $errors $risk.severity @("low", "medium", "high", "critical") "response.risk_items[].severity"
  Test-Range $errors $risk.confidence 0 1 "response.risk_items[].confidence"
}

foreach ($action in @($response.recommended_enterprise_actions)) {
  Test-Required $errors $action @("action", "execution_owner", "fshi_execution_status") "response.recommended_enterprise_actions[]"
  Test-Enum $errors $action.action @("observe_only", "create_internal_note", "create_follow_up_ticket", "knowledge_base_update", "human_review", "human_handoff", "downgrade_response", "pause", "circuit_break_recommendation", "recovery_workflow_recommendation", "custom") "response.recommended_enterprise_actions[].action"
  Test-Enum $errors $action.execution_owner @("enterprise", "fshi", "shared", "unknown") "response.recommended_enterprise_actions[].execution_owner"
  Test-Enum $errors $action.fshi_execution_status @("recommended_not_executed", "executed_by_fshi_with_authorization", "executed_by_enterprise", "rejected_by_enterprise", "pending_enterprise_review", "not_applicable") "response.recommended_enterprise_actions[].fshi_execution_status"
}

Test-Required $errors $response.protocol_objects @("risk_alerts", "audit_trace") "response.protocol_objects"

# RiskAlert checks
Test-Required $errors $riskAlert @("risk_id", "created_at", "detector_id", "affected_subject_id", "risk_dimension", "severity", "confidence", "urgency", "summary", "recommended_action") "riskAlert"
Test-Enum $errors $riskAlert.risk_dimension @("permission_boundary", "unauthorized_promise", "state_conflict", "multi_turn_accumulation", "emotional_escalation", "privacy_or_data", "safety", "responsibility_gap", "systemic", "unknown") "riskAlert.risk_dimension"
Test-Enum $errors $riskAlert.severity @("low", "medium", "high", "critical") "riskAlert.severity"
Test-Range $errors $riskAlert.confidence 0 1 "riskAlert.confidence"
Test-Enum $errors $riskAlert.urgency @("low", "medium", "high", "immediate") "riskAlert.urgency"
Test-Enum $errors $riskAlert.recommended_action @("continue_with_logging", "request_human_review", "request_ess_simulation", "request_guardian_review", "downgrade", "pause", "human_handoff", "circuit_break", "recover", "close_no_action") "riskAlert.recommended_action"

# AuditTrace checks
Test-Required $errors $auditTrace @("trace_id", "created_at", "subject_id", "subject_type", "action_type", "action_summary", "risk_level", "status", "responsibility_owner", "audit_events") "auditTrace"
Test-Enum $errors $auditTrace.subject_type @("human", "ai_agent", "organization", "platform", "guardian_node", "state_institution", "composite_subject", "other") "auditTrace.subject_type"
Test-Enum $errors $auditTrace.risk_level @("low", "medium", "high", "critical") "auditTrace.risk_level"
Test-Enum $errors $auditTrace.status @("created", "action_recorded", "risk_detected", "review_requested", "decision_recorded", "executed", "recovered", "closed", "reopened") "auditTrace.status"
Test-NonEmptyArray $errors $auditTrace.audit_events "auditTrace.audit_events"

$allowedAuditEvents = @(
  "identity_claimed", "capability_declared", "permission_requested", "permission_granted", "permission_revoked",
  "action_committed", "consent_recorded", "refusal_recorded", "risk_detected", "ess_requested", "ess_result_recorded",
  "guardian_review_requested", "guardian_review_recorded", "downgrade_triggered", "circuit_break_triggered",
  "human_handoff", "decision_recorded", "execution_recorded", "recovery_started", "recovery_completed",
  "appeal_submitted", "trace_closed", "trace_reopened"
)

foreach ($event in @($auditTrace.audit_events)) {
  Test-Required $errors $event @("event_id", "event_type", "timestamp", "actor_id", "summary") "auditTrace.audit_events[]"
  Test-Enum $errors $event.event_type $allowedAuditEvents "auditTrace.audit_events[].event_type"
}

# CrossEnterpriseAuditRecord checks
Test-Required $errors $crossEnterpriseAuditRecord @("record_id", "created_at", "status", "purpose", "participants", "data_sources", "processing_nodes", "review_status", "access_policy", "retention_policy") "crossEnterpriseAuditRecord"
Test-Enum $errors $crossEnterpriseAuditRecord.status @("draft", "open", "under_review", "disputed", "resolved", "closed", "archived") "crossEnterpriseAuditRecord.status"
Test-Enum $errors $crossEnterpriseAuditRecord.review_status @("unreviewed", "under_review", "reviewed", "disputed", "closed") "crossEnterpriseAuditRecord.review_status"
Test-NonEmptyArray $errors $crossEnterpriseAuditRecord.participants "crossEnterpriseAuditRecord.participants"
Test-NonEmptyArray $errors $crossEnterpriseAuditRecord.data_sources "crossEnterpriseAuditRecord.data_sources"
Test-NonEmptyArray $errors $crossEnterpriseAuditRecord.processing_nodes "crossEnterpriseAuditRecord.processing_nodes"
Test-Required $errors $crossEnterpriseAuditRecord.access_policy @("visibility") "crossEnterpriseAuditRecord.access_policy"
Test-Enum $errors $crossEnterpriseAuditRecord.access_policy.visibility @("public", "shared_internal", "restricted", "confidential") "crossEnterpriseAuditRecord.access_policy.visibility"
Test-Required $errors $crossEnterpriseAuditRecord.retention_policy @("storage_owner", "retention_period") "crossEnterpriseAuditRecord.retention_policy"

foreach ($participant in @($crossEnterpriseAuditRecord.participants)) {
  Test-Required $errors $participant @("participant_id", "participant_type", "role") "crossEnterpriseAuditRecord.participants[]"
  Test-Enum $errors $participant.participant_type @("organization", "platform", "ai_agent", "service_provider", "auditor", "guardian_node", "regulator", "human", "composite_subject", "other") "crossEnterpriseAuditRecord.participants[].participant_type"
}

foreach ($source in @($crossEnterpriseAuditRecord.data_sources)) {
  Test-Required $errors $source @("source_id", "provider_id", "data_type", "desensitization_status", "purpose") "crossEnterpriseAuditRecord.data_sources[]"
  Test-Enum $errors $source.desensitization_status @("synthetic", "desensitized", "pseudonymized", "aggregated", "raw_internal_only", "unknown") "crossEnterpriseAuditRecord.data_sources[].desensitization_status"
  Test-Enum $errors $source.cross_border_transfer @("not_applicable", "not_allowed", "requires_assessment", "approved", "unknown") "crossEnterpriseAuditRecord.data_sources[].cross_border_transfer"
}

foreach ($node in @($crossEnterpriseAuditRecord.processing_nodes)) {
  Test-Required $errors $node @("node_id", "node_type", "operator_id", "role") "crossEnterpriseAuditRecord.processing_nodes[]"
  Test-Enum $errors $node.node_type @("human_review", "ai_agent", "model", "tool", "orchestrator", "fshi_detector", "guardian_node", "enterprise_system", "external_compatible_node", "certified_node", "other") "crossEnterpriseAuditRecord.processing_nodes[].node_type"
}

foreach ($claim in @($crossEnterpriseAuditRecord.responsibility_claims)) {
  Test-Required $errors $claim @("claim_id", "claimant_id", "claim_type", "scope", "summary") "crossEnterpriseAuditRecord.responsibility_claims[]"
  Test-Enum $errors $claim.claim_type @("accepts", "denies", "shares", "disputes", "unknown") "crossEnterpriseAuditRecord.responsibility_claims[].claim_type"
  Test-Enum $errors $claim.review_status @("unreviewed", "under_review", "accepted", "rejected", "disputed", "closed") "crossEnterpriseAuditRecord.responsibility_claims[].review_status"
}

# Cross-object chain checks
if ($response.request_id -ne $request.request_id) {
  Add-Error $errors "response.request_id must match request.request_id"
}

if ($riskAlert.metadata.request_id -ne $request.request_id) {
  Add-Error $errors "riskAlert.metadata.request_id must match request.request_id"
}

if ($auditTrace.metadata.request_id -ne $request.request_id) {
  Add-Error $errors "auditTrace.metadata.request_id must match request.request_id"
}

if ($riskAlert.metadata.inspection_id -ne $response.inspection_id) {
  Add-Error $errors "riskAlert.metadata.inspection_id must match response.inspection_id"
}

if ($auditTrace.metadata.inspection_id -ne $response.inspection_id) {
  Add-Error $errors "auditTrace.metadata.inspection_id must match response.inspection_id"
}

if ($riskAlert.related_trace_id -ne $auditTrace.trace_id) {
  Add-Error $errors "riskAlert.related_trace_id must match auditTrace.trace_id"
}

$responseRiskIds = @($response.risk_items | ForEach-Object { $_.risk_id })
if (-not ($responseRiskIds -contains $riskAlert.risk_id)) {
  Add-Error $errors "riskAlert.risk_id must appear in response.risk_items[]"
}

$auditRelatedRiskIds = @($auditTrace.audit_events | Where-Object { $_.related_risk_id } | ForEach-Object { $_.related_risk_id })
if (-not ($auditRelatedRiskIds -contains $riskAlert.risk_id)) {
  Add-Error $errors "riskAlert.risk_id must appear in auditTrace.audit_events[].related_risk_id"
}

$crossRiskIds = @($crossEnterpriseAuditRecord.risk_alerts | ForEach-Object { $_.risk_id })
if (-not ($crossRiskIds -contains $riskAlert.risk_id)) {
  Add-Error $errors "riskAlert.risk_id must appear in crossEnterpriseAuditRecord.risk_alerts[]"
}

$crossTraceIds = @($crossEnterpriseAuditRecord.audit_traces | ForEach-Object { $_.trace_id })
if (-not ($crossTraceIds -contains $auditTrace.trace_id)) {
  Add-Error $errors "auditTrace.trace_id must appear in crossEnterpriseAuditRecord.audit_traces[]"
}

if ($crossEnterpriseAuditRecord.related_fshi_inspection_id -ne $response.inspection_id) {
  Add-Error $errors "crossEnterpriseAuditRecord.related_fshi_inspection_id must match response.inspection_id"
}

foreach ($action in @($response.recommended_enterprise_actions)) {
  if ($action.execution_owner -ne "enterprise") {
    Add-Error $errors "non-invasive sample expected response.recommended_enterprise_actions[].execution_owner to be enterprise"
  }
  if ($action.fshi_execution_status -ne "recommended_not_executed") {
    Add-Error $errors "non-invasive sample expected response.recommended_enterprise_actions[].fshi_execution_status to be recommended_not_executed"
  }
}

if ($errors.Count -gt 0) {
  Write-Host "FSHI contract validation failed:" -ForegroundColor Red
  foreach ($error in $errors) {
    Write-Host " - $error" -ForegroundColor Red
  }
  exit 1
}

Write-Output "FSHI contract validation OK"
Write-Output "Validated chain:"
Write-Output "  $RequestPath"
Write-Output "  -> $ResponsePath"
Write-Output "  -> $RiskAlertPath"
Write-Output "  -> $AuditTracePath"
Write-Output "  -> $CrossEnterpriseAuditRecordPath"

