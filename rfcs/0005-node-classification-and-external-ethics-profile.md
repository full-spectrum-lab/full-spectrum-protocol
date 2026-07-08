# RFC 0005: Node Classification and External Ethics Profile

> Status: Draft  
> Created: 2026-06-29  
> Related RFCs:
> - [RFC 0001: Full Spectrum Protocol](./0001-full-spectrum-protocol.md)
> - [RFC 0002: Identity and Capability Declaration](./0002-identity-and-capability-declaration.md)
> - [RFC 0003: Audit Trace Schema](./0003-audit-trace-schema.md)
> - [RFC 0004: RiskAlert Schema](./0004-risk-alert-schema.md)
> Related schema:
> - [`schemas/external-ethics-profile.schema.json`](../schemas/external-ethics-profile.schema.json)

---

## 1. Summary

This RFC defines a node classification model for the Full Spectrum Protocol and introduces the `ExternalEthicsProfile` object.

The goal is to keep Full Spectrum open and interoperable without diluting the meaning of Full Spectrum certified digital identity.

This RFC distinguishes:

- **External Tool Node**: a tool or model used without Full Spectrum digital identity;
- **External Compatible Node**: an external node that does not sign the Full Spectrum Agent Protocol Stack, but declares its own ethics, audit, risk, and responsibility mechanisms in a mappable form;
- **Candidate Node**: a node under observation before full certification;
- **Full Spectrum Certified Node**: a node that signs or equivalently satisfies Full Spectrum protocol requirements and can be trusted for higher-consequence contexts.

This RFC also defines how consequence level affects identity, authorization, audit, and review requirements.

---

## 2. Motivation

Full Spectrum is intended to be a bridge, not a forced center.

If every organization were required to sign the full Full Spectrum Agent Protocol Stack before any interaction, the protocol would become too rigid and would fail to interoperate with existing systems.

If every external system could claim compatibility without structured disclosure, the protocol would be diluted and could become a tool for ethics-washing.

This RFC creates a middle path:

- external tools can remain tools;
- external systems can declare compatible mappings;
- certified nodes retain a higher trust status;
- high-consequence actions require stronger identity, authorization, audit, and review.

---

## 3. Design principles

### 3.1 Bridge, not cage

Full Spectrum does not require every AI system, organization, or agent to become Full Spectrum native.

It provides a protocol language for identity, capability, authorization, risk, responsibility, and review.

### 3.2 Compatibility is not certification

An external compatible node may interoperate with Full Spectrum systems, but it must not claim to be a Full Spectrum certified digital identity.

### 3.3 Responsibility scales with consequence

Higher-consequence actions require stronger authorization, audit, review, and recovery mechanisms.

### 3.4 No consequence, no forced binding

Low-impact tools should not be forced into a heavy identity system.

However, once a tool output is adopted into a consequential workflow, the adopting subject becomes responsible for the adoption decision.

### 3.5 Modules should not swallow the whole

Each protocol module should constrain its own scope. No single module should become a global control mechanism.

---

## 4. Node classes

### 4.1 External Tool Node

An External Tool Node is a tool, model, script, service, or temporary computational node without Full Spectrum digital identity.

Typical use:

- drafting;
- internal brainstorming;
- summarization;
- formatting;
- low-impact classification;
- non-consequential computation.

Rules:

- it may be used as a tool;
- it must not claim Full Spectrum certification;
- it does not independently hold Full Spectrum digital identity;
- if its output is adopted into a consequential action, responsibility moves to the adopting subject.

Recommended audit handling:

- record tool name or identifier if available;
- record version or model family if available;
- record caller or adopting subject;
- record whether the tool output was accepted, modified, rejected, or escalated.

### 4.2 External Compatible Node

An External Compatible Node is a node that does not sign the full Full Spectrum Agent Protocol Stack, but submits an External Ethics Profile.

Typical use:

- an organization with its own AI ethics and audit framework;
- an enterprise system that wants to interoperate without adopting Full Spectrum as its internal governance doctrine;
- an external agent platform that can map its identity, audit, risk, and responsibility fields to Full Spectrum objects.

Rules:

- it may interoperate within declared scope;
- it must submit an External Ethics Profile;
- it must disclose gaps and conflicts;
- it must not claim Full Spectrum certification;
- it should be restricted from high-consequence or critical actions unless equivalent controls are verified.

### 4.3 Candidate Node

A Candidate Node is a node under observation before Full Spectrum certification.

Typical use:

- limited trial operation;
- low- or medium-consequence scenarios;
- audit trace accumulation;
- capability and boundary verification.

Rules:

- it has a provisional identity;
- it must declare capability and boundary;
- it must generate AuditTrace for relevant actions;
- it may be upgraded, downgraded, suspended, or rejected based on evidence.

### 4.4 Full Spectrum Certified Node

A Full Spectrum Certified Node is a node that signs or equivalently satisfies Full Spectrum protocol requirements.

Minimum requirements:

- identity anchor;
- capability declaration;
- boundary declaration;
- authorization source;
- responsibility chain;
- AuditTrace support;
- RiskAlert support;
- downgrade, revocation, and recovery mechanism;
- protocol commitment or equivalence proof.

Additional requirements for high-consequence contexts may include:

- FSHI or equivalent health/risk/audit capability check;
- human or organizational authorization anchor;
- guardian or independent review;
- epistemic boundary declaration;
- stronger recovery and appeal mechanisms.

---

## 5. Consequence levels

Consequence level determines the minimum required node class and control strength.

| Consequence level | Example | Minimum requirement |
| --- | --- | --- |
| none | private draft, internal brainstorming | External Tool Node |
| low | low-impact classification, formatting, non-sensitive advice | External Tool Node or External Compatible Node |
| medium | customer-service risk flag, workflow recommendation, non-binding risk analysis | External Compatible Node; AuditTrace recommended or required by context |
| high | credit, medical, hiring, procurement, legal, finance, permission change | Full Spectrum Certified Node or verified equivalent controls |
| critical | automatic circuit-break, public impact, irreversible action, major resource allocation | certified node, strong authorization, review, revocation, and recovery |

Consequence level should not be determined only by action type. The downstream adoption path must also be considered.

For example, a text-generation action may appear low consequence, but become high consequence if adopted into a legal, medical, financial, or public-facing decision.

---

## 6. External Ethics Profile

An External Ethics Profile is a structured declaration by an external compatible node.

It should answer:

- Who operates this node?
- Who authorized it?
- What can it do?
- What can it not do?
- How are actions recorded?
- How are risks classified?
- Who is responsible for negative consequences?
- How are data retained and deleted?
- Which Full Spectrum requirements are equivalent?
- Which requirements are missing?
- Which requirements conflict?
- How are conflicts resolved?
- How can the node be downgraded, revoked, or recovered?

The related machine-readable schema is:

- [`external-ethics-profile.schema.json`](../schemas/external-ethics-profile.schema.json)

---

## 7. Compatibility boundaries

External compatibility should not become unlimited permission.

Some gaps may be acceptable:

- different identity format;
- different audit storage mechanism;
- different risk labels if mappable;
- different review workflow if auditable.

Some gaps require restriction:

- no responsibility chain;
- no audit log;
- no risk handling;
- no revocation path;
- no data retention policy.

Some conflicts may be incompatible:

- refusal to identify a responsible operator;
- denial of user notice in consequential contexts;
- systematic prevention of review, appeal, or correction;
- permission to execute high-consequence actions without authorization;
- risk handling that hides material harm or prevents traceability.

---

## 8. Misrepresentation

A compatible node must not describe itself as:

- Full Spectrum certified;
- Full Spectrum digital identity;
- guardian-approved;
- FSHI-verified;
- protocol-native;

unless it has completed the relevant requirements.

Misrepresentation should be recorded as a risk and may trigger:

- compatibility suspension;
- public correction;
- audit escalation;
- downgrade of trust status.

---

## 9. Relation to digital identity

Full Spectrum digital identity is not a normal account or API key.

It implies:

- identity;
- authorization;
- capability boundary;
- responsibility;
- auditability;
- risk handling;
- revocation;
- recovery;
- rights or protections appropriate to the node class.

An AI system that has not signed or equivalently satisfied the relevant protocol requirements may still exist and operate as a tool, but it should not receive Full Spectrum certified digital identity.

---

## 10. Relation to FSHI

FSHI may be used as an engineering sample and verification mechanism for risk detection and audit capability.

For high-consequence digital identity, FSHI or an equivalent health/risk/audit capability check may be required.

This RFC does not make FSHI the only possible verification method. Equivalent mechanisms may be accepted if they provide comparable evidence.

---

## 11. Security and abuse considerations

Risks:

- ethics-washing through weak compatibility declarations;
- hiding high-consequence actions under low-consequence labels;
- using external tools as responsibility escape routes;
- claiming certification without review;
- declaring compatibility while omitting audit, risk, or responsibility mechanisms.

Mitigations:

- require External Ethics Profile;
- separate compatibility from certification;
- record adoption responsibility;
- classify consequence by downstream effect;
- require stronger controls for high and critical consequence contexts;
- record misrepresentation as a risk event.

---

## 12. Open questions

1. Who evaluates whether an External Ethics Profile is sufficient?
2. Should compatibility be self-declared, community-reviewed, or guardian-reviewed?
3. What is the minimum audit field set for medium-consequence compatible nodes?
4. What consequence-level thresholds should trigger mandatory certification?
5. How should compatibility expire or require renewal?
6. How should disagreement between external ethics systems be logged?

---

## 13. Acceptance criteria

This RFC is useful if it enables:

- clear distinction between tools, compatible nodes, candidates, and certified nodes;
- machine-readable external ethics profiles;
- safer compatibility without forced adoption;
- protection of Full Spectrum certified digital identity from dilution;
- practical examples and minimal demos.


