# Full Spectrum Protocol

[![Validate protocol contracts](https://github.com/full-spectrum-lab/full-spectrum-protocol/actions/workflows/validate.yml/badge.svg)](https://github.com/full-spectrum-lab/full-spectrum-protocol/actions/workflows/validate.yml)
[![Schema checks](https://github.com/full-spectrum-lab/full-spectrum-protocol/actions/workflows/schema-check.yml/badge.svg)](https://github.com/full-spectrum-lab/full-spectrum-protocol/actions/workflows/schema-check.yml)

> An open governance semantics protocol for AI-era subjects: humans, AI agents, organizations, systems, and cross-organization networks.

Full Spectrum Protocol is a bridge, not a forced center. It does not replace law, regulation, enterprise compliance, A2A, MCP, national agent-interconnection standards, or human judgment. It defines a governance layer above connectivity: action basis, boundary declaration, risk visibility, audit trace, responsibility path, and review interface.

Chinese readers can start from [README.zh-CN.md](./README.zh-CN.md). English readers may also use [README.en.md](./README.en.md).

## Start in 10 minutes

| Goal | Entry |
|---|---|
| Understand the protocol boundary | [START_HERE](./START_HERE.md) |
| Inspect the ecommerce object chain | [examples/cases/ecommerce_chain](./examples/cases/ecommerce_chain/README.md) |
| Validate current schemas | [tools/validate_schemas.py](./tools/validate_schemas.py) |
| Read the I/O contract | [specs/io-contract.md](./specs/io-contract.md) |
| Run the reference observer | [full-spectrum-engine](https://github.com/full-spectrum-lab/full-spectrum-engine#quick-start) |

---

## Current status

This repository is an early open protocol draft and engineering exploration.

It currently provides:

- protocol outlines and RFCs;
- machine-readable schemas;
- synthetic examples;
- mapping documents for standards and business scenarios;
- a reference direction for FSHI customer-service inspection;
- links to a minimal runnable governance engine;
- shared ecosystem diagrams and public-facing commons assets.

It does not claim:

- to be a finished global standard;
- to be approved by any regulator;
- to replace legal, safety, compliance, or human review processes;
- to contain mature commercial product code;
- to prove that any person, group, or system can represent “the whole.”

---

## Why this exists

Modern AI systems are becoming faster, more autonomous, and more deeply embedded in real organizations. Existing interoperability work can help agents discover each other, communicate, call tools, and exchange task states.

Full Spectrum focuses on the next layer:

- Why was this action allowed?
- Who or what is acting?
- What capability and boundary were declared?
- What risk was detected?
- Who is accountable if harm occurs?
- What should be recorded for later review?
- When should an agent slow down, downgrade, stop, or ask for human review?
- When should a system know that it does not know enough to act?

The short version:

> Connectivity lets agents act together. Full Spectrum asks how connected agents remain auditable, accountable, and boundary-aware.

---

## What this project is not

Full Spectrum is not:

- a new religion or spiritual authority;
- a world government;
- a replacement for law, human rights, safety regulation, or enterprise compliance;
- a finished AI safety solution;
- a commercial SaaS product;
- a claim that all external systems must join a Full Spectrum network;
- a claim that “having a protocol” means an AI system is safe.

It is a protocol draft, schema set, and open engineering path for making AI-related actions more visible, reviewable, and accountable.

---

## Relationship to standards and ecosystems

Full Spectrum does not replace A2A, MCP, LangGraph, national agent-interconnection standards, data-governance systems, or AI risk frameworks.

Those systems mainly answer connectivity and infrastructure questions:

- how agents identify themselves;
- how capabilities are described;
- how agents discover one another;
- how messages and tasks are exchanged;
- how tools are invoked;
- how data is governed and transferred.

Full Spectrum focuses on the governance layer around those interactions:

- action basis;
- risk declaration;
- audit trace;
- responsibility path;
- boundary awareness;
- review and escalation;
- cross-organization audit envelopes.

See:

- [Protocol Mapping Center](./docs/mapping/README.md)
- [Standards and ecosystem mapping](./docs/mapping/standards-mapping.md)
- [Cross-Enterprise Audit Record Mapping](./docs/mapping/cross-enterprise-audit-record-mapping.md)
- [FSHI API Contract Mapping](./docs/mapping/fshi-api-contract-mapping.md)

---

## 30-second entry path

- If you are only calling an external AI tool, start with [External Node Guide](./EXTERNAL_NODE_GUIDE.md).
- If you operate an existing AI system and want compatibility without full certification, start with [RFC 0005](./rfcs/0005-node-classification-and-external-ethics-profile.md).
- If you need a shared audit envelope across organizations, start with [RFC 0006](./rfcs/0006-cross-enterprise-audit-record.md).
- If you need identity and capability declarations, start with [RFC 0002](./rfcs/0002-identity-and-capability-declaration.md).
- If you need risk and audit objects, start with [RFC 0003](./rfcs/0003-audit-trace-schema.md) and [RFC 0004](./rfcs/0004-risk-alert-schema.md).
- If you need to understand subject levels versus node types, start with [Subject Levels and Node Types](./docs/guides/subject-levels-and-node-types.md).
- If you want a business-facing example, start with [FSHI API Contract Mapping](./docs/mapping/fshi-api-contract-mapping.md).
- If you want to improve the protocol, start with [RFC 0001](./rfcs/0001-full-spectrum-protocol.md).

---

## Minimal governance chain

A minimal Full Spectrum-compatible flow can be described as:

```text
Raw AI Action
  -> Governance Event
  -> Business Adapter
  -> Canonical Context
  -> Layer Profile
  -> Engine / Policy / Safety Check
  -> RiskAlert / AuditTrace / Runestone
  -> Human or organizational review
```

The current project does not require a system to join a global protocol network before trying this flow. A company or developer can first run a local-first engine internally, using synthetic or desensitized data.

---

## Protocol map

| Layer | Question | Typical artifacts |
| --- | --- | --- |
| Identity | Who or what is acting? | Identity claim, digital identity declaration |
| Capability | What can it do? | Capability declaration, boundary statement |
| Permission | What is allowed now? | Authorization, consent, revocation |
| Responsibility | Who is accountable? | AuditTrace, responsibility path |
| Simulation | What may happen under different conditions? | ESS-style scenario simulation |
| Risk | When should action slow, downgrade, stop, or escalate? | RiskAlert, circuit-break, recovery report |
| Review | Who reviews conflict when no single subject should decide alone? | Guardian review, organizational review, human review |
| Evolution | How does the protocol change without becoming a new cage? | RFCs, versioning, counterexamples |

---

## Engineering reference: FSHI

FSHI, the Full Spectrum Health Index, is used here as an engineering reference for AI customer-service quality inspection.

In this repository, FSHI is:

- a protocol use case;
- a synthetic and desensitized example direction;
- an API-contract mapping exercise;
- an example of non-invasive multi-turn dialogue risk detection;
- a bridge from governance semantics to business engineering.

It is not presented here as a complete commercial product implementation.

Suggested boundary:

- `full-spectrum-protocol`: protocol, schemas, RFCs, examples, audit format.
- `full-spectrum-engine`: minimal runnable local-first governance engine.
- private/company repositories: customer adapters, production deployment, commercial assets, and real enterprise data.

---

## Local-first adoption path

Full Spectrum should not force adoption. Protocol compatibility does not create a networking, public-identity, or certification obligation.

A practical adoption path is:

1. **Internal observer layer**: run the engine locally on enterprise-controlled, synthetic, or desensitized data.
2. **Optional local declaration**: attach an enterprise-local subject, capability, boundary, unknown policy, and responsible-human reference when attribution is needed.
3. **Stable contracts**: use I/O envelopes, Profiles, replay, and audit before attempting broader integration.
4. **Optional protocol execution/network**: add certified identity or cross-node interoperability only when a real cross-organization requirement exists.

The first-generation observer can operate without public DID, external certification, community membership, or protocol-network participation.

See also:

- [Three-Layer Evolution Path](./docs/guides/three-layer-evolution-path.md)
- [Subject Levels and Node Types](./docs/guides/subject-levels-and-node-types.md)

## Evidence and research boundary

- [Evidence and Project Status](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/evidence-and-status.md) separates implemented artifacts from hypotheses.
- [Public Working Paper WP-001](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/research/working-papers/wp-001-governance-semantics-and-local-observer-engine.md) describes the current object chain and observer boundary; it is not peer reviewed.
- Older civilization-dynamics and RG manuscripts remain under editorial review and are not protocol specifications or engineering proof.

---

## Machine validation

This repository currently validates:

- common mojibake patterns in Markdown, JSON, YAML, HTML, CSS, and script files;
- schema/sample consistency for selected protocol objects;
- the FSHI dialogue inspection contract chain:

```text
request.sample.json
  -> response.sample.json
  -> risk-alert.sample.json
  -> audit-trace.sample.json
  -> cross-enterprise-audit-record.example.json
```

Validation runs through GitHub Actions on push and pull request to `main`.

---

## Start here

Recommended reading order:

1. [START_HERE.md](./START_HERE.md)
2. [Documentation index](./docs/README.md)
3. [Full Spectrum Protocol Outline v0.1](./docs/protocols/full-spectrum-protocol-outline-v0.1.md)
4. [Glossary](./docs/glossary.md)
5. [Specifications](./specs/README.md)
6. [External Node Guide](./EXTERNAL_NODE_GUIDE.md)
7. [RFC 0001: Full Spectrum Protocol](./rfcs/0001-full-spectrum-protocol.md)
8. [RFC 0002: Identity and Capability Declaration](./rfcs/0002-identity-and-capability-declaration.md)
9. [RFC 0003: Audit Trace Schema](./rfcs/0003-audit-trace-schema.md)
10. [RFC 0004: RiskAlert Schema](./rfcs/0004-risk-alert-schema.md)
11. [RFC 0005: Node Classification and External Ethics Profile](./rfcs/0005-node-classification-and-external-ethics-profile.md)
12. [RFC 0006: Cross-Enterprise Audit Record Profile](./rfcs/0006-cross-enterprise-audit-record.md)
13. [Protocol Mapping Center](./docs/mapping/README.md)
14. [FSHI customer-service quality inspection use case](./docs/use-cases/FSHI_Customer_Service_Quality_Inspection.md)
15. [Conformance and Testing Guide](./docs/testing/conformance-and-testing-guide.md)
16. [Validations](./validations/)
17. [ROADMAP.md](./ROADMAP.md)

---

## Contributing

Contributions, critiques, translations, schemas, examples, and counterexamples are welcome.

Please read:

- [CONTRIBUTING.md](./CONTRIBUTING.md)
- [GOVERNANCE.md](./GOVERNANCE.md)
- [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)

---

## Safety note

Do not store tokens, passwords, cookies, private keys, unredacted personal information, unauthorized enterprise data, or real customer data in this repository.


