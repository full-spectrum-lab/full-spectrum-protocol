# Full Spectrum Protocol FAQ

This FAQ is written for first-time readers, developers, researchers, enterprise reviewers, and AI agents inspecting this repository.

---

## 1. What is Full Spectrum Protocol?

Full Spectrum Protocol is an open governance semantics protocol for AI-era subjects.

It is designed to describe and record:

- who or what is acting;
- what capability and boundary were declared;
- why an action was allowed or blocked;
- what risk was detected;
- who is accountable;
- what should be reviewed later;
- when an AI system should slow down, downgrade, stop, or ask for human review.

It is not a single model, product, law, or ideology.

---

## 2. Is this an AI safety standard?

No.

It is a protocol draft and engineering exploration. It may help express parts of an AI governance process, but it does not replace formal AI safety standards, legal obligations, compliance reviews, regulatory requirements, or human judgment.

---

## 3. Does Full Spectrum replace A2A, MCP, or national agent-interconnection standards?

No.

A2A, MCP, and national agent-interconnection standards mainly address connectivity:

- agent identity;
- capability description;
- discovery;
- message exchange;
- task interaction;
- tool invocation.

Full Spectrum focuses on the governance layer around connected actions:

- action basis;
- risk declaration;
- audit trace;
- responsibility path;
- review and escalation;
- boundary awareness.

The relationship is complementary, not competitive.

---

## 4. Must an enterprise join a Full Spectrum network to use the engine?

No.

The practical adoption path is local-first:

1. run a local engine internally;
2. test with synthetic or desensitized cases;
3. generate RiskAlert / AuditTrace / Runestone outputs;
4. decide whether any external compatibility or certification is needed later.

Joining a protocol network is a later optional layer, not a prerequisite for internal use.

---

## 5. What is `full-spectrum-engine`?

`full-spectrum-engine` is a minimal runnable governance engine for experimenting with Full Spectrum concepts.

It is not the whole protocol and not a mature commercial product.

It demonstrates how governance events, risks, boundaries, scenario simulation, and audit outputs can be processed in code.

---

## 6. What is FSHI?

FSHI means Full Spectrum Health Index.

In this repository, FSHI is used as an engineering reference for AI customer-service quality inspection. It demonstrates how desensitized multi-turn dialogue, business state, risk signals, and audit outputs can be mapped into protocol objects.

It does not mean that a complete commercial product or private company implementation lives in this repository.

---

## 7. Does the protocol make final decisions?

No.

The protocol helps make risks, boundaries, decision basis, and responsibility paths visible. Final decisions remain with the relevant human, organization, legal process, regulator, or authorized governance process.

---

## 8. What is a Governance Event?

A Governance Event is a minimal record of an AI-related action that may need governance review.

It typically includes:

- actor;
- action;
- context;
- declared capability;
- declared boundary;
- risk indicators;
- decision basis;
- review requirement;
- audit output.

It is the entry object for turning “an AI did something” into “a reviewable governance record.”

---

## 9. What is a node?

A node can be a tool, an AI system, an organization, or another subject that participates in a governance relationship.

Not all nodes need the same level of constraint.

Low-consequence tools may only need external compatibility. High-consequence agents may need identity binding, capability declaration, review paths, and stronger audit requirements.

---

## 10. What is the difference between external, compatible, candidate, and certified nodes?

Short version:

- **External tool node**: can be called as a tool; no Full Spectrum identity is implied.
- **Compatible node**: declares external ethics/profile compatibility but is not fully certified.
- **Candidate node**: is preparing for stronger identity, boundary, and audit requirements.
- **Certified node**: satisfies stronger protocol constraints for high-consequence use.

See [External Node Guide](../../EXTERNAL_NODE_GUIDE.md).

---

## 11. What is the role of “compassion” in the protocol?

“Compassion” here is not a moral slogan.

It means a system-level constraint:

- preserve overall continuity;
- maximally respect free will;
- dynamically accommodate differences;
- avoid letting efficiency erase concrete subjects, rights, or responsibility.

In engineering documents, this should be interpreted through boundaries, auditability, review, and consequence tracking.

---

## 12. Can this protocol prove an AI is safe?

No.

It can help record and inspect certain governance conditions. It cannot guarantee safety, correctness, fairness, legality, or moral truth.

---

## 13. Can the protocol be used without sharing private data?

Yes.

The recommended first step is to use synthetic or desensitized data. Real enterprise data should remain under the enterprise’s own legal, security, and privacy controls.

---

## 14. What can be open sourced?

Generally suitable for open source:

- protocol drafts;
- schemas;
- synthetic examples;
- validation scripts;
- documentation;
- minimal runtime engine;
- adapters without private customer logic.

Not suitable for open source:

- real customer data;
- enterprise secrets;
- private deployment credentials;
- internal business rules;
- tokens, keys, cookies, passwords;
- unauthorized logs.

---

## 15. What is the current project stage?

Early protocol draft and alpha-stage engineering exploration.

The project is ready for review, critique, synthetic testing, schema validation, and small local experiments. It is not yet a mature production standard.


