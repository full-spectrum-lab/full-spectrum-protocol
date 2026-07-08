# External Node Guide

This guide explains how external tools, compatible systems, candidate nodes, and Full Spectrum certified nodes should be described in this repository.

Full Spectrum is a bridge protocol, not a forced center.

External systems may choose:

- not to adopt Full Spectrum;
- to map their own ethics and audit framework into Full Spectrum objects;
- to become Full Spectrum certified for higher-consequence contexts.

Compatibility is not certification.

---

## 1. Adoption paths

Full Spectrum can be adopted in stages. A system does not need to join the Full Spectrum protocol network in order to use a local engine or map its own governance records.

### 1.1 Stage 0: internal engine use

An organization may deploy a Full Spectrum-compatible engine internally to support its own business workflows.

Typical use:

- offline or internal risk inspection;
- customer-service quality review;
- synthetic case testing;
- internal AuditTrace generation;
- local ESS-style scenario review;
- internal compliance reporting.

Stage 0 does not create a Full Spectrum network identity.

Stage 0 does not imply certification.

Stage 0 outputs are local governance artifacts unless the organization later chooses to publish, export, or map them into a wider protocol context.

### 1.2 Stage 1: compatible integration

An organization may keep its own ethics, compliance, and operational rules while mapping selected fields into Full Spectrum objects such as:

- GovernanceEvent;
- RiskAlert;
- AuditTrace;
- CrossEnterpriseAuditRecord;
- ExternalEthicsProfile.

This path is suitable when a system wants interoperability without signing the full Full Spectrum Agent Protocol Stack.

Stage 1 compatibility means: "we can speak selected Full Spectrum protocol objects."

It does not mean: "we are Full Spectrum certified."

### 1.3 Stage 2: certified network participation

A node may apply for Full Spectrum certified status when it needs higher-consequence participation, cross-node trust, or protocol-network recognition.

This may require:

- identity anchoring;
- authorization source;
- protocol commitments;
- capability and boundary declaration;
- RiskAlert and AuditTrace conformance;
- review and recovery procedures;
- human or organizational responsibility binding where required;
- certification, suspension, downgrade, and revocation rules.

Stage 2 is optional. It should be used only when the node needs the trust level and responsibility boundary that certification provides.

---

## 2. Node classes

### 2.1 External Tool Node

An External Tool Node is a tool or model without Full Spectrum digital identity.

Examples:

- text drafting;
- summarization;
- formatting;
- internal brainstorming;
- low-impact classification.

It may be used as a tool, but it must not claim Full Spectrum certification.

If its output is adopted into a consequential workflow, the adopting human, organization, or certified node becomes responsible for that adoption decision.

### 2.2 External Compatible Node

An External Compatible Node does not sign the full Full Spectrum Agent Protocol Stack, but declares its own ethics, audit, risk, and responsibility framework through an External Ethics Profile.

It may interoperate within declared scope.

It must not claim to be a Full Spectrum certified digital identity.

### 2.3 Candidate Node

A Candidate Node is under observation before certification.

It can run in limited low- or medium-consequence contexts while accumulating audit traces and demonstrating capability boundaries.

### 2.4 Full Spectrum Certified Node

A Full Spectrum Certified Node signs or equivalently satisfies the relevant Full Spectrum protocol requirements.

It may be eligible for higher-consequence contexts depending on its authorization, audit, review, and risk-handling strength.

---

## 3. Consequence levels

| Level | Examples | Typical node requirement |
| --- | --- | --- |
| none | private draft, internal brainstorming | external tool |
| low | formatting, non-sensitive classification | external tool or compatible node |
| medium | customer-service risk flag, workflow recommendation | compatible node with AuditTrace |
| high | credit, medical, hiring, procurement, legal, finance | certified node or verified equivalent controls |
| critical | automatic circuit-break, irreversible public impact | strong certification, authorization, review, recovery |

Consequence is not determined only by the immediate action. Downstream adoption matters.

A low-impact generated text can become high-consequence if used in a legal, financial, medical, hiring, or public-facing decision.

---

## 4. External Ethics Profile

External Compatible Nodes should submit an External Ethics Profile.

Minimum contents:

- identity anchor;
- authorization source;
- capability and limitation statement;
- supported consequence levels;
- audit log structure;
- risk classification;
- responsibility or liability assignment;
- data retention and deletion policy;
- equivalency map to Full Spectrum requirements;
- missing items;
- conflict items;
- incompatible clauses;
- conflict resolution rule;
- downgrade, revocation, and recovery path.

Machine-readable schema:

- [`schemas/external-ethics-profile.schema.json`](./schemas/external-ethics-profile.schema.json)

Example:

- [`examples/governance/external-ethics-profile.example.json`](./examples/governance/external-ethics-profile.example.json)

---

## 5. What compatible nodes may say

Allowed:

> This node has submitted an External Ethics Profile for Full Spectrum compatibility mapping.

Allowed:

> This node maps selected audit and risk fields to Full Spectrum AuditTrace and RiskAlert objects.

Not allowed unless certified:

> This node is Full Spectrum certified.

Not allowed unless certified:

> This node has Full Spectrum certified digital identity.

---

## 6. When compatibility is not enough

Compatibility may be insufficient when:

- there is no responsible operator;
- no audit log exists;
- risks are not classified;
- high-consequence actions can be executed without authorization;
- users are denied notice or review in consequential contexts;
- downgrade, revocation, or recovery is impossible;
- the node claims certification without evidence.

High- and critical-consequence contexts may require Full Spectrum certification or verified equivalent controls.

---

## 7. Practical first step

For early adopters:

1. Decide whether the current goal is Stage 0 internal use, Stage 1 compatible integration, or Stage 2 certified network participation.
2. Identify the node class.
3. Declare the highest consequence level it may touch.
4. Fill an External Ethics Profile if not Full Spectrum native.
5. Map audit logs to AuditTrace if possible.
6. Map risk events to RiskAlert if possible.
7. Do not claim certification unless certification requirements are met.

