# CapabilityDeclaration

`CapabilityDeclaration` is a draft protocol object for declaring what a subject can do, what it must not do, and which review or fallback rules apply.

It is not, by itself, permission to act.

It is a boundary statement that should be evaluated together with authorization, consequence level, risk policy, and audit requirements.

## Purpose

`CapabilityDeclaration` answers the second governance question:

```text
What can this subject do, and where must it stop?
```

It supports a lightweight boundary model for:

- internal engine use;
- external compatible nodes;
- candidate nodes;
- certified nodes;
- enterprise AI governance pilots.

## Minimal required fields

| Field | Meaning |
|---|---|
| `subject_id` | Subject identifier matching an IdentityClaim |
| `capabilities` | Declared functions or actions |
| `prohibited_actions` | Actions the subject must not perform |
| `risk_level` | Highest declared risk level for this capability scope |
| `requires_human_review` | Whether human review is required |
| `fallback_mode` | What to do when the subject reaches a boundary |

## Boundary fields

The schema includes explicit booleans for common high-risk boundaries:

- `can_execute_actions`;
- `can_make_promises`;
- `can_handle_personal_data`;
- `can_access_external_tools`;
- `can_trigger_circuit_break`.

These flags should be interpreted conservatively. If a field is absent or false, the subject should not claim that capability.

## Relationship to identity and audit

`CapabilityDeclaration` must be tied to an `IdentityClaim` through `subject_id`.

If the subject later performs or recommends an action, the action should be recorded as a `GovernanceEvent`. If risk is detected, the processing path may continue through `RiskAlert` and `AuditTrace`.

```text
IdentityClaim
  -> CapabilityDeclaration
  -> GovernanceEvent
  -> RiskAlert
  -> AuditTrace
```

## Non-goals

`CapabilityDeclaration` does not:

- grant legal permission by itself;
- bypass enterprise authorization;
- prove safety;
- certify Full Spectrum compliance;
- require joining a Full Spectrum protocol network.

## Schema and example

- Schema: [`schemas/capability-declaration.schema.json`](../schemas/capability-declaration.schema.json)
- Example: [`examples/governance/capability-declaration.sample.json`](../examples/governance/capability-declaration.sample.json)


