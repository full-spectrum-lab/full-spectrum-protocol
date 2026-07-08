# RFC 0006: Cross-Enterprise Audit Record Profile

> Status: Draft  
> Created: 2026-07-03  
> Related RFCs:
> - [RFC 0001: Full Spectrum Protocol](./0001-full-spectrum-protocol.md)
> - [RFC 0003: Audit Trace Schema](./0003-audit-trace-schema.md)
> - [RFC 0004: RiskAlert Schema](./0004-risk-alert-schema.md)
> - [RFC 0005: Node Classification and External Ethics Profile](./0005-node-classification-and-external-ethics-profile.md)
> Related schema:
> - [`schemas/cross-enterprise-audit-record.schema.json`](../schemas/cross-enterprise-audit-record.schema.json)

---

## 1. Summary

This RFC defines a draft profile for a `CrossEnterpriseAuditRecord`.

The purpose is to make cross-organization AI audit records inspectable, comparable, and reviewable without forcing every participant to expose raw data, adopt the same internal system, or sign the same full ethics stack.

This profile is intended for scenarios where multiple organizations, agents, platforms, service providers, or review nodes participate in one consequential workflow and need a shared audit envelope.

Examples:

- an enterprise AI customer-service workflow involving a platform, merchant, logistics provider, and third-party AI service;
- a cross-border procurement agent involving buyer, supplier, payment provider, and compliance reviewer;
- an FSHI inspection task where risk alerts and audit traces must be shared with more than one accountable party;
- a multi-agent workflow where responsibility is distributed across orchestration, tool invocation, model output, and human review.

This RFC is not a legal standard. It is a profile draft for interoperable audit records.

---

## 2. Motivation

Existing AI interoperability standards and protocols can help agents discover each other, describe capabilities, invoke tools, and exchange messages.

However, once a cross-enterprise workflow produces a risk, dispute, compliance question, customer complaint, financial consequence, or safety concern, the hard question changes:

- Which parties participated?
- Which data sources were used?
- Which node produced which output?
- Which risk was detected?
- Which audit trace records the action?
- Which party accepts, denies, shares, or disputes responsibility?
- Which evidence can be shared, and which must remain private?
- Who is allowed to review, retain, export, or delete the record?

Without a shared audit profile, each organization may keep its own logs, but those logs may not line up. Responsibility can disappear between systems.

This RFC creates a lightweight shared envelope for cross-enterprise audit interoperability.

---

## 3. Design goals

### 3.1 Shared envelope, not shared database

The profile does not require all parties to use the same database.

It defines a record shape that can reference local logs, redacted evidence, risk alerts, audit traces, contracts, permissions, and review outcomes.

### 3.2 Data minimization by default

The record should carry enough metadata to support audit and review, but should not expose unnecessary personal data, commercial secrets, raw dialogue, model prompts, or internal system details.

Evidence may be referenced rather than embedded.

### 3.3 Responsibility visibility

The profile must make responsibility claims visible.

It does not decide who is legally responsible. It records who claims responsibility, who disputes it, what evidence exists, and which review process is pending or complete.

### 3.4 Interoperability with existing protocol objects

The profile should connect to:

- `RiskAlert`;
- `AuditTrace`;
- FSHI inspection request and response;
- `ExternalEthicsProfile`;
- identity and capability declarations;
- enterprise compliance logs.

### 3.5 Compatible without forced certification

External compatible nodes may participate by mapping their own audit objects into this profile.

Full Spectrum certified nodes may provide stronger guarantees, but certification is not required for every participant in every record.

---

## 4. Core object

The core object is `CrossEnterpriseAuditRecord`.

At minimum, it should describe:

- record identity;
- purpose and case context;
- participants;
- data sources;
- processing nodes;
- risk alerts;
- audit traces;
- responsibility claims;
- dispute status;
- access policy;
- retention policy.

The related schema is:

- [`cross-enterprise-audit-record.schema.json`](../schemas/cross-enterprise-audit-record.schema.json)

---

## 5. Participants

Participants may include:

- organizations;
- platforms;
- AI agents;
- service providers;
- auditors;
- guardian nodes;
- regulators;
- humans;
- composite subjects.

Each participant should declare:

- participant identifier;
- participant type;
- role in the workflow;
- jurisdiction if relevant;
- responsibility owner if different from the participant itself;
- contact or reference if lawful and appropriate.

Participant inclusion does not imply blame.

It means the participant is materially relevant to the workflow or review.

---

## 6. Data sources

Data sources should be described without unnecessary exposure.

Each data source should record:

- source identifier;
- provider;
- data type;
- desensitization or minimization status;
- purpose of use;
- time range if applicable;
- data residency or storage region if relevant;
- cross-border transfer status if relevant.

The record should support both embedded evidence summaries and external evidence references.

For high-risk or regulated contexts, raw data should normally remain inside the responsible organization unless lawful sharing is explicitly authorized.

---

## 7. Processing nodes

Processing nodes are systems, agents, tools, or human review steps that transform, classify, decide, recommend, execute, or review.

Each processing node should record:

- node identifier;
- node type;
- operator or responsible owner;
- input references;
- output references;
- role in the workflow;
- whether it is external, compatible, candidate, or certified if known.

This avoids treating an AI workflow as a single opaque system when responsibility is actually distributed across many nodes.

---

## 8. Risk and audit linkage

The profile should link, not duplicate, existing risk and audit objects.

Recommended linkage:

- `risk_alerts[]` references `RiskAlert` objects by ID or embeds minimized alert summaries;
- `audit_traces[]` references `AuditTrace` objects by ID or embeds minimized trace summaries;
- `related_fshi_inspection_id` links to an FSHI response if the record came from a dialogue inspection;
- `related_case_id` links to a local case, ticket, complaint, procurement request, or review item.

When records are exchanged across organizations, redacted summaries may be shared while full traces remain in the source system.

---

## 9. Responsibility claims

Responsibility is not always singular.

This profile supports multiple responsibility claims:

- accepts responsibility;
- denies responsibility;
- shares responsibility;
- disputes responsibility;
- unknown or pending.

A responsibility claim should include:

- claimant;
- claim type;
- scope;
- summary;
- evidence references;
- review status.

The profile does not automatically resolve disputes. It makes the dispute visible and reviewable.

---

## 10. Access and retention

Every record should include access and retention policies.

Access policy should define:

- visibility level;
- allowed participants;
- redacted fields;
- export restrictions;
- review permissions.

Retention policy should define:

- storage owner;
- retention period;
- deletion or review date;
- legal hold status if applicable.

This is especially important for cross-enterprise and cross-border workflows.

---

## 11. Relationship to national standards and internal systems

This profile does not replace national standards, enterprise compliance systems, contracts, regulators, or courts.

It is designed to sit above connection and identity layers and below legal judgment.

For example:

- a national agent interoperability standard may define how an agent is identified and invoked;
- enterprise systems may define internal workflow rules;
- Full Spectrum objects may define risk, audit, review, and responsibility fields;
- legal or compliance authorities decide final enforceable outcomes.

The profile only provides a shared audit envelope for parties that need to compare records.

---

## 12. Security and abuse considerations

Risks:

- using audit records as a substitute for actual responsibility;
- exposing sensitive data through excessive evidence sharing;
- misrepresenting partial audit records as complete truth;
- hiding responsibility behind external tools or compatible nodes;
- creating inconsistent records across organizations;
- treating a profile draft as a binding legal standard.

Mitigations:

- require data minimization notes;
- distinguish references from embedded evidence;
- record unresolved disputes;
- track responsibility claims separately from legal conclusions;
- include access and retention policies;
- make profile status explicit as draft unless formally adopted.

---

## 13. Open questions

1. What minimum field set should be required for regulated industries?
2. How should two organizations reconcile conflicting audit records?
3. Should record signatures be required for high-consequence contexts?
4. How should redaction be represented in a machine-readable way?
5. How should cross-border evidence references be handled?
6. When should guardian or independent review be required?
7. How should this profile map to specific national standards and enterprise platforms?

---

## 14. Acceptance criteria

This RFC is useful if it enables:

- a shared cross-enterprise audit envelope;
- machine-readable validation;
- safer sharing without raw data exposure;
- visible responsibility claims and disputes;
- linkage to RiskAlert and AuditTrace;
- practical use by FSHI, multi-agent governance, and enterprise compliance workflows.


