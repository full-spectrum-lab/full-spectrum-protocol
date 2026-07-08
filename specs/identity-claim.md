# IdentityClaim

`IdentityClaim` is a draft protocol object for declaring who or what is acting in a Full Spectrum-compatible context.

It is not, by itself, a certification.

It is a structured identity statement that can be issued by a human, organization, platform, governance system, or another accountable issuer.

## Purpose

`IdentityClaim` answers the first governance question:

```text
Who is the acting subject?
```

It may describe:

- a human;
- an AI agent;
- an organization;
- a platform;
- a guardian node;
- a state institution;
- a composite subject;
- another declared subject type.

## Minimal required fields

| Field | Meaning |
|---|---|
| `subject_id` | Stable identifier for the subject within the issuing context |
| `subject_type` | Type of subject |
| `display_name` | Human-readable name |
| `issuer` | Who issued this identity claim |
| `issued_at` | When the claim was issued |
| `responsibility_owner` | Human, organization, or accountable entity responsible for the subject |
| `audit_required` | Whether actions from this subject require AuditTrace records |

## Trust boundary

An `IdentityClaim` can be self-claimed, issuer-verified, guardian-verified, or institution-verified.

These levels are not equal.

A self-claimed identity may be useful for internal testing or Stage 0 engine use. High-consequence contexts may require stronger verification, human or organizational responsibility binding, and additional review.

## Relationship to capability declaration

`IdentityClaim` says who the subject is.

`CapabilityDeclaration` says what the subject claims it can do, what it must not do, and when review is required.

```text
IdentityClaim
  -> CapabilityDeclaration
  -> GovernanceEvent
  -> RiskAlert
  -> AuditTrace
```

## Non-goals

`IdentityClaim` does not:

- prove legal identity by itself;
- grant authorization by itself;
- certify Full Spectrum compliance;
- replace national identity, enterprise identity, or regulatory identity systems.

## Schema and example

- Schema: [`schemas/identity-claim.schema.json`](../schemas/identity-claim.schema.json)
- Example: [`examples/governance/identity-claim.sample.json`](../examples/governance/identity-claim.sample.json)


