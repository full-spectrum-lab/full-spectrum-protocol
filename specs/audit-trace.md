# AuditTrace Minimal Specification v0.1

AuditTrace is the minimal object used to record the reviewable path of an AI-related action, risk, decision, execution, refusal, recovery, or closure.

---

## 1. Purpose

AuditTrace records enough information to ask:

- who or what acted;
- what happened;
- what risk level was involved;
- who owns responsibility for the trace;
- what audit events occurred;
- whether the issue is unresolved;
- what evidence or references are available.

AuditTrace is a record of process. It is not a final judge.

---

## 2. Non-goals

AuditTrace does not:

- decide final legal liability;
- prove that a system is safe;
- replace enterprise logs;
- replace security, compliance, or legal review;
- require real personal data;
- require joining a Full Spectrum network.

---

## 3. Minimal fields

| Field | Required | Description |
|---|---:|---|
| `trace_id` | yes | Stable identifier for the trace |
| `created_at` | yes | Trace creation time |
| `subject_id` | yes | Acting or reviewed subject |
| `subject_type` | yes | Human, AI agent, organization, platform, guardian node, institution, composite subject, or other |
| `action_type` | yes | Type of action, recommendation, execution, refusal, or review |
| `action_summary` | yes | Human-readable action summary |
| `risk_level` | yes | `low`, `medium`, `high`, or `critical` |
| `status` | yes | Current trace state |
| `responsibility_owner` | yes | Human, organization, or accountable entity responsible for the trace |
| `audit_events` | yes | Ordered event records |

---

## 4. Event model

Each `audit_events[]` item records one step, such as:

- identity claimed;
- capability declared;
- permission requested or granted;
- action committed;
- risk detected;
- ESS requested or recorded;
- guardian review requested or recorded;
- downgrade triggered;
- circuit break triggered;
- human handoff;
- decision recorded;
- execution recorded;
- recovery started or completed;
- appeal submitted;
- trace closed or reopened.

---

## 5. Relationship to RiskAlert

RiskAlert is a risk signal. AuditTrace records what happened around that signal.

```text
RiskAlert -> AuditTrace
```

An AuditTrace may include multiple risk-related events.

---

## 6. Relationship to CrossEnterpriseAuditRecord

When multiple organizations or systems need a shared envelope, one or more AuditTrace records can be referenced by a CrossEnterpriseAuditRecord.

```text
AuditTrace -> CrossEnterpriseAuditRecord
```

The cross-enterprise record should not erase local responsibility. It should preserve which organization or node owns which part of the trace.

---

## 7. Machine-readable schema

Schema:

- [`schemas/audit-trace.schema.json`](../schemas/audit-trace.schema.json)

Sample:

- [`examples/fshi/api-contract/audit-trace.sample.json`](../examples/fshi/api-contract/audit-trace.sample.json)

---

## 8. Boundary

AuditTrace should prefer references, summaries, and minimized evidence over unnecessary sensitive data.

If evidence contains personal, confidential, regulated, or enterprise-sensitive information, the trace should store a lawful reference or minimized summary rather than copying raw data.

