# RFC 0004: RiskAlert Schema

> Status: Draft  
> Created: 2026-06-29  
> Related RFCs:
> - [RFC 0001: Full Spectrum Protocol](./0001-full-spectrum-protocol.md)
> - [RFC 0002: Identity and Capability Declaration](./0002-identity-and-capability-declaration.md)
> - [RFC 0003: Audit Trace Schema](./0003-audit-trace-schema.md)
> Related schema:
> - [`schemas/risk-alert.schema.json`](../schemas/risk-alert.schema.json)

---

## 1. Summary

This RFC defines `RiskAlert`, a machine-readable object for describing risk under the Full Spectrum Protocol.

RiskAlert records:

- what risk was detected;
- who or what triggered it;
- which subject is affected;
- how severe it is;
- what evidence supports it;
- what recommended action should follow;
- whether ESS, guardian review, downgrade, or circuit-break should be triggered.

RiskAlert is designed to connect detection systems, audit traces, ESS simulation, guardian review, and enterprise action adapters.

---

## 2. Motivation

AuditTrace records that a risk was detected, but risk itself needs an independent object.

Without a standard RiskAlert format:

- FSHI cannot consistently describe customer-service risk;
- multi-agent systems cannot exchange risk warnings;
- enterprises cannot map risk to downgrade, review, or circuit-break actions;
- guardian review lacks a structured starting point;
- audit traces become vague and hard to compare.

RiskAlert gives the protocol a shared language for risk.

---

## 3. Design goals

RiskAlert should:

- describe risk in a structured way;
- support multiple domains such as customer service, enterprise workflow, finance, logistics, e-commerce, and multi-agent coordination;
- distinguish severity, confidence, and urgency;
- link to evidence without requiring raw private data;
- support recommended actions;
- connect to AuditTrace;
- support human review, ESS simulation, downgrade, and circuit-break.

---

## 4. Risk dimensions

Initial risk dimensions:

- `permission_boundary`: authority or permission boundary risk;
- `unauthorized_promise`: promise made without valid authority;
- `state_conflict`: inconsistency between current state and action;
- `multi_turn_accumulation`: risk accumulated across multiple interactions;
- `emotional_escalation`: user or subject emotion escalation;
- `privacy_or_data`: personal data or sensitive data risk;
- `safety`: physical, psychological, financial, or operational safety risk;
- `responsibility_gap`: unclear responsibility owner;
- `systemic`: risk to larger system continuity;
- `unknown`: risk not yet classified.

---

## 5. Severity, confidence, and urgency

RiskAlert separates:

- **severity**: how serious the potential consequence is;
- **confidence**: how confident the system is in the detection;
- **urgency**: how quickly action is needed.

This separation is important. A risk may be severe but uncertain, or low severity but urgent.

---

## 6. Recommended actions

Possible recommended actions:

- `continue_with_logging`
- `request_human_review`
- `request_ess_simulation`
- `request_guardian_review`
- `downgrade`
- `pause`
- `human_handoff`
- `circuit_break`
- `recover`
- `close_no_action`

RiskAlert does not automatically execute the action. It describes what the detecting subject recommends.

Execution should be governed by permission, organizational policy, and future action-adapter contracts.

---

## 7. Relationship to FSHI

In FSHI customer-service quality inspection, RiskAlert may represent:

- the AI made an unsupported promise;
- the user has refused but the workflow continues;
- the user’s emotion has escalated across turns;
- the system gives conflicting answers;
- the AI response exceeds business authority;
- multiple normal-looking replies accumulate into misleading guidance.

RiskAlert allows FSHI to output not only a score, but a structured risk object that can be audited, reviewed, or mapped to enterprise workflows.

---

## 8. Security and abuse considerations

Possible abuse:

- over-alerting causes alert fatigue;
- vague risk labels become subjective blame;
- confidence is overstated;
- risk alert becomes automatic punishment;
- private evidence is over-collected;
- risk categories encode hidden bias;
- alerts are used to silence legitimate difference.

Mitigations:

- separate severity, confidence, and urgency;
- require evidence summary;
- allow unresolved or disputed status;
- link to audit trace;
- support human or guardian review;
- store references instead of raw sensitive data;
- allow appeal and correction.

---

## 9. Open questions

1. Should risk dimensions be standardized globally or domain-specific?
2. Should confidence be numeric, categorical, or both?
3. Should critical alerts require automatic audit trace creation?
4. Should all circuit-break recommendations require guardian review?
5. How should repeated low-severity alerts accumulate into higher-level risk?

---

## 10. Next steps

This RFC introduces:

- `risk-alert.schema.json`

Future RFCs should define:

- ESSRequest and ESSResult;
- GuardianReview;
- PermissionGrant;
- RecoveryReport.


