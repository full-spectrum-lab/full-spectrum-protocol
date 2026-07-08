# FSHI Customer-Service Quality Inspection Use Case

FSHI means Full Spectrum Health Index.

In this repository, FSHI is used as an engineering use case for applying the Full Spectrum Protocol to AI customer-service quality inspection.

## Why this use case matters

Customer-service conversations are a practical place where AI, humans, organizations, rules, promises, emotions, permissions, and responsibility meet.

A single answer may look correct, but risk may accumulate across turns:

- user frustration may escalate;
- the system may make promises without authority;
- a workflow may continue even after the user refuses;
- different knowledge sources may conflict;
- business responsibility may become unclear;
- an AI agent may exceed its boundary.

FSHI is designed to inspect these multi-turn risks without replacing the enterprise's existing customer-service system.

## Non-invasive design

The preferred early design is non-invasive:

1. The enterprise exports desensitized dialogue data.
2. FSHI receives only necessary fields.
3. FSHI performs offline or API-based inspection.
4. FSHI outputs risk items, explanations, and recommended actions.
5. The enterprise decides whether and how to execute actions.

FSHI does not need to control the enterprise's customer-service AI in the first stage.

## What FSHI can inspect

Typical inspection dimensions:

- single-turn compliance;
- multi-turn risk accumulation;
- state conflict;
- wrong or unauthorized promise;
- user emotion escalation;
- permission boundary crossing;
- responsibility path ambiguity;
- unresolved or looping dialogue;
- need for downgrade, human review, or circuit-break.

## Relationship to the Full Spectrum Protocol

FSHI is not only a quality-inspection tool. It is a cell-level application of the Full Spectrum Protocol.

| Full Spectrum concept | FSHI mapping |
| --- | --- |
| Identity | customer, agent, human service, organization |
| Capability | what the AI/customer-service process can handle |
| Boundary | what it must not promise or execute |
| Permission | what actions are authorized under current state |
| Audit | dialogue trace, risk trace, responsibility trace |
| ESS | scenario simulation for possible consequence paths |
| Circuit-break | downgrade, pause, human takeover, recovery |
| Guardian review | manual review, business owner review, expert review |

## Logistics and e-commerce adapters

Industry adapters should be plug-in style.

If an enterprise has rich industry fields, the adapter can use them.

If it does not, FSHI should fall back to a general inspection mode.

Suggested adapter strategy:

- general core first;
- logistics adapter as a field and terminology package;
- e-commerce adapter as a knowledge-source and order-state package;
- no hard dependency on one industry's workflow.

## API contract mapping

The API-facing contract is described in:

- [FSHI API Contract Mapping](../mapping/fshi-api-contract-mapping.md)

The mapping separates:

- enterprise input fields;
- FSHI inspection output;
- Full Spectrum `RiskAlert`;
- Full Spectrum `AuditTrace`;
- enterprise-side execution or refusal.

FSHI may recommend downgrade, handoff, follow-up, or review, but enterprise execution remains under enterprise authorization unless a separate production integration contract exists.

## Repository boundary

This repository should contain:

- protocol explanation;
- sample data format;
- sample output format;
- schema direction;
- minimal examples;
- public demo links.

This repository should not contain:

- real customer data;
- private enterprise adapters;
- full commercial deployment code;
- secrets, keys, or internal credentials.

If FSHI becomes an open-source engineering project, a separate repository such as `fshi-open-core` is recommended.

