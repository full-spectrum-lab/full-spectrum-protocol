# RFC 0002: Identity and Capability Declaration

> Status: Draft  
> Created: 2026-06-29  
> Related RFC: [RFC 0001: Full Spectrum Protocol](./0001-full-spectrum-protocol.md)  
> Related schemas:
> - [`schemas/identity-claim.schema.json`](../schemas/identity-claim.schema.json)
> - [`schemas/capability-declaration.schema.json`](../schemas/capability-declaration.schema.json)

---

## 1. Summary

This RFC defines the first machine-readable objects in the Full Spectrum Protocol:

1. **IdentityClaim**: who or what is interacting.
2. **CapabilityDeclaration**: what the subject can do, cannot do, and under what boundary conditions.

These objects are the foundation for permission, responsibility, risk review, audit trace, and guardian review.

---

## 2. Motivation

High-risk human-AI and multi-agent systems often fail because the acting subject is unclear.

Examples:

- an AI agent gives advice but its authority source is unknown;
- an enterprise workflow executes an action but responsibility is unclear;
- a user believes they are talking to a human, but the responder is an AI;
- a system makes a promise that it has no authority to make;
- a tool or agent continues acting after its mission or permission has expired.

Before a system can ask “what is allowed?”, it must answer:

> Who is acting, what can it do, what can it not do, and who is responsible for it?

---

## 3. Design goals

The declaration format should:

- support humans, AI agents, organizations, platforms, guardian nodes, and composite subjects;
- be readable by both humans and machines;
- support legal or organizational jurisdiction fields without replacing law;
- declare responsibility owner;
- declare capability and boundary;
- indicate whether audit is required;
- support expiration and revocation;
- remain simple enough for early implementation.

---

## 4. IdentityClaim

IdentityClaim declares the acting subject.

Minimum fields:

- `subject_id`
- `subject_type`
- `display_name`
- `issuer`
- `issued_at`
- `responsibility_owner`
- `audit_required`

Optional but recommended fields:

- `expires_at`
- `jurisdiction`
- `trust_level`
- `guardian_verified`
- `related_documents`
- `metadata`

Subject types may include:

- `human`
- `ai_agent`
- `organization`
- `platform`
- `guardian_node`
- `state_institution`
- `composite_subject`
- `other`

---

## 5. CapabilityDeclaration

CapabilityDeclaration declares what the subject can and cannot do.

Minimum fields:

- `subject_id`
- `capabilities`
- `prohibited_actions`
- `risk_level`
- `requires_human_review`
- `fallback_mode`

Optional but recommended fields:

- `required_permissions`
- `can_execute_actions`
- `can_make_promises`
- `can_handle_personal_data`
- `can_access_external_tools`
- `can_trigger_circuit_break`
- `domain_scope`
- `valid_from`
- `valid_until`
- `recovery_contact`
- `metadata`

---

## 6. Boundary rules

A capability declaration must not only list what a subject can do. It must also list what it cannot do.

For AI agents, important boundaries include:

- whether the agent can execute external actions;
- whether it can make promises on behalf of an organization;
- whether it can process personal data;
- whether it can trigger downgrade or circuit-break;
- whether it requires human review above a risk threshold.

For organizations, important boundaries include:

- which business domain is covered;
- who owns responsibility;
- which legal or policy jurisdiction applies;
- what data can be shared;
- which actions are only advisory.

---

## 7. Relationship to permission

Identity and capability do not automatically grant permission.

They only describe:

- who the subject is;
- what it is technically or organizationally capable of;
- what boundaries it declares.

Actual permission should be granted through a separate `PermissionGrant` object in future RFCs.

---

## 8. Security and abuse considerations

Possible abuse:

- false identity declaration;
- exaggerated capability;
- missing prohibited actions;
- unclear responsibility owner;
- expired identity still being used;
- low-risk label hiding high-risk behavior;
- organization using an AI agent as a responsibility shield.

Mitigation:

- required issuer;
- audit-required flag;
- expiration field;
- guardian verification field;
- responsibility owner field;
- capability/prohibited-action pair;
- future audit trace linkage.

---

## 9. Open questions

1. Should `trust_level` be standardized or left to each ecosystem?
2. Should human subjects be required to disclose real identity, pseudonymous identity, or context identity?
3. How should guardian verification be represented?
4. How should revoked identities be published?
5. Should capability declarations be signed?

---

## 10. Next steps

This RFC introduces two draft schemas:

- `identity-claim.schema.json`
- `capability-declaration.schema.json`

Future RFCs should define:

- PermissionGrant;
- AuditTrace;
- RiskAlert;
- ESSRequest / ESSResult;
- GuardianReview.


