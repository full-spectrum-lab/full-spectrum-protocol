# RFC 0003: Audit Trace Schema

> Status: Draft  
> Created: 2026-06-29  
> Related RFCs:
> - [RFC 0001: Full Spectrum Protocol](./0001-full-spectrum-protocol.md)
> - [RFC 0002: Identity and Capability Declaration](./0002-identity-and-capability-declaration.md)
> Related schema:
> - [`schemas/audit-trace.schema.json`](../schemas/audit-trace.schema.json)

---

## 1. Summary

This RFC defines `AuditTrace`, a machine-readable record of a high-risk or reviewable interaction under the Full Spectrum Protocol.

AuditTrace records:

- who acted;
- under what identity;
- with what declared capability;
- under what permission;
- what action was taken;
- what risk was detected;
- whether consent, refusal, or appeal occurred;
- whether ESS or guardian review was triggered;
- what outcome occurred;
- what recovery or follow-up is required.

AuditTrace is the foundation for responsibility visibility.

---

## 2. Motivation

In complex human-AI and multi-agent systems, many failures are not caused by one clearly malicious action.

They are caused by invisible chains:

- authority slowly expands;
- risk accumulates across turns;
- no one knows who approved an action;
- a user’s refusal is not recorded;
- an AI agent makes a promise without authority;
- a system downgrades or escalates without explanation;
- review happens informally and cannot be reconstructed.

Without audit trace, responsibility disappears.

The Full Spectrum Protocol requires that high-risk interaction leave a structured trace.

---

## 3. Design goals

AuditTrace should:

- connect identity, capability, permission, action, risk, review, and outcome;
- support both human-readable and machine-readable review;
- record uncertainty and unresolved conflict;
- support legal, organizational, and technical audit;
- avoid storing unnecessary sensitive data;
- work for both offline inspection and real-time systems;
- support future linking to RiskAlert, ESSResult, GuardianReview, and RecoveryReport.

---

## 4. Trace lifecycle

A typical AuditTrace may follow this lifecycle:

1. `created`: trace is opened.
2. `action_recorded`: an action or recommendation is recorded.
3. `risk_detected`: risk is detected or updated.
4. `review_requested`: ESS, human, or guardian review is requested.
5. `decision_recorded`: decision or recommendation is recorded.
6. `executed`: action is executed, if execution occurs.
7. `recovered`: recovery or repair is completed.
8. `closed`: trace is closed.
9. `reopened`: trace is reopened due to appeal, dispute, or new evidence.

---

## 5. Minimum fields

Minimum required fields:

- `trace_id`
- `created_at`
- `subject_id`
- `subject_type`
- `action_type`
- `action_summary`
- `risk_level`
- `status`
- `responsibility_owner`
- `audit_events`

---

## 6. Audit events

An AuditTrace contains an ordered list of audit events.

Each audit event should include:

- `event_id`
- `event_type`
- `timestamp`
- `actor_id`
- `summary`

Optional event fields:

- `related_permission_id`
- `related_risk_id`
- `related_ess_id`
- `related_guardian_review_id`
- `evidence_uri`
- `metadata`

---

## 7. Event types

Initial event types:

- `identity_claimed`
- `capability_declared`
- `permission_requested`
- `permission_granted`
- `permission_revoked`
- `action_committed`
- `consent_recorded`
- `refusal_recorded`
- `risk_detected`
- `ess_requested`
- `ess_result_recorded`
- `guardian_review_requested`
- `guardian_review_recorded`
- `downgrade_triggered`
- `circuit_break_triggered`
- `human_handoff`
- `decision_recorded`
- `execution_recorded`
- `recovery_started`
- `recovery_completed`
- `appeal_submitted`
- `trace_closed`
- `trace_reopened`

---

## 8. Privacy and data minimization

AuditTrace should not become a surveillance database.

It should record the minimum information needed to reconstruct responsibility and risk.

Recommended practices:

- store references to evidence instead of raw sensitive content where possible;
- use desensitized or hashed identifiers when appropriate;
- separate customer data from protocol trace data;
- avoid recording private content unless necessary for review;
- define retention periods;
- allow lawful deletion or redaction where applicable.

---

## 9. Relationship to FSHI

In FSHI customer-service quality inspection, AuditTrace can record:

- dialogue sample identifier;
- AI or human service identity;
- detected risk category;
- multi-turn accumulation path;
- unauthorized promise;
- user refusal or escalation;
- recommendation for downgrade or human review;
- manual review result;
- final outcome.

This allows FSHI to explain not only “what risk was found”, but “how the risk emerged and who should review it”.

---

## 10. Security and abuse considerations

Possible abuse:

- audit data becomes excessive surveillance;
- trace is modified after the fact;
- responsibility owner is falsely assigned;
- sensitive data is stored unnecessarily;
- systems generate traces too vague to be useful;
- audit trace is used to blame individuals while hiding organizational responsibility.

Mitigations:

- append-only event model where possible;
- signed or hashed trace snapshots in high-risk environments;
- required responsibility owner;
- data minimization;
- explicit unresolved-state flag;
- separation of protocol audit from raw private data;
- guardian or human review for disputed traces.

---

## 11. Open questions

1. Should AuditTrace be append-only by default?
2. Should trace snapshots be signed?
3. How long should audit traces be retained?
4. How should personal data redaction be handled?
5. How should multiple organizations share a cross-boundary trace?
6. How should conflicting responsibility claims be represented?

---

## 12. Next steps

This RFC introduces:

- `audit-trace.schema.json`

Future RFCs should define:

- RiskAlert;
- ESSRequest and ESSResult;
- GuardianReview;
- RecoveryReport.


