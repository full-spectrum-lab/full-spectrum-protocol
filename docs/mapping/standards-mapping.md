# Standards and Ecosystem Mapping

Status: draft  
Last updated: 2026-06-30

This document maps the Full Spectrum Ethics Protocol Stack to existing standards, public policy directions, and agent engineering ecosystems.

It is not a legal opinion, certification claim, or replacement for national standards. It is a positioning document for protocol review.

---

## 1. Core positioning

Most current agent standards and frameworks focus on the interconnection layer:

- How does an agent identify itself?
- How does it describe its capabilities?
- How does it discover other agents or tools?
- How does it communicate and invoke tools?
- How does a workflow engine orchestrate multiple agents?

Full Spectrum focuses on the governance layer above and around interconnection:

- Why was this action allowed?
- Which rule, authorization, or scenario supported it?
- Who is accountable if the result causes harm?
- What risk was detected before action?
- What cost, responsibility, refusal, escalation, downgrade, circuit-break, review, recovery, or rollback should be recorded?
- When should an agent know that it does not know, or should not act?

Short form:

> AIP/A2A/MCP-style protocols answer “can agents connect and act?” Full Spectrum explores “how should connected agents remain auditable, accountable, and boundary-aware?”

---

## 2. China AIP national standard series

China has released the national standard series **Artificial Intelligence — Agent Interconnection** (`人工智能 智能体互联`), covering:

- general architecture;
- identity code;
- identity management;
- agent description;
- agent discovery;
- agent interaction;
- agent tool invocation.

These standards establish an interconnection baseline for agent identity, capability description, discovery, collaboration, and tool calling.

Full Spectrum should not duplicate this layer. It should treat AIP-style identity and interoperability objects as possible anchors.

| AIP area | Interconnection question | Full Spectrum complement |
| --- | --- | --- |
| Identity code | Which agent is this? | `agent_did`, human/org responsibility anchor, certification status |
| Identity management | How is the agent identity managed? | consent, authorization, revocation, responsibility path |
| Agent description | What can the agent do? | capability declaration, boundary declaration, forbidden actions |
| Agent discovery | How do agents find each other? | compatibility class: tool node, compatible node, candidate node, certified node |
| Agent interaction | How do agents exchange tasks or messages? | AuditTrace, RiskAlert, ESS request/result, guardian review |
| Tool invocation | How does an agent call external tools? | permission check, risk check, rollback/recovery record, refusal path |

Design implication:

> Full Spectrum should be able to reference or anchor to external identity and interconnection standards, rather than issuing a competing identity universe.

Implementation note:

> In domestic or regulated deployments, a Full Spectrum DID should anchor to the applicable AIP-style identity code and enterprise legal identifier where required. The local identity system remains the authority of record; Full Spectrum adds audit, responsibility, boundary, and review metadata.

---

## 3. Data element infrastructure and data-governance trend

China’s public policy direction around data elements emphasizes data circulation, authorized use, scenario-based application, and data as an input for AI development.

This document intentionally does **not** claim that any specific “national data group” has been officially established unless an authoritative public source is available. For now, the safer positioning is:

> Data-element infrastructure and data-governance policy are strengthening the “AI fuel layer”. Full Spectrum focuses on the governance record that should accompany consequential data use.

Possible Full Spectrum complements:

| Data-governance area | Typical question | Full Spectrum complement |
| --- | --- | --- |
| Data authorization | Was data use authorized? | consent record, permission record, refusal record |
| Data circulation | Where did data move? | AuditTrace, source/target record, responsibility path |
| Data risk | What risk appeared during use? | RiskAlert, downgrade/circuit-break recommendation |
| Data value/cost | What value or cost did data use create? | frequency economy / EC-FC accounting concept |
| Data dispute | Who reviews conflicts? | guardian review, human review, appeal path |

Implementation note:

> EC/FC and AuditTrace records may themselves become regulated decision data. Their retention, export, cross-border transfer, and regulatory disclosure should follow applicable data-governance, privacy, cybersecurity, sectoral, and local jurisdiction requirements.

---

## 4. A2A, MCP, and agent engineering frameworks

Full Spectrum is not a replacement for A2A, MCP, workflow engines, or observability platforms.

It is better positioned as a governance payload and audit layer that can be attached to them.

| Ecosystem layer | What it primarily does | Full Spectrum complement |
| --- | --- | --- |
| A2A-style protocols | Agent-to-agent discovery, task exchange, interoperability | responsibility, risk, refusal, cost, review, boundary awareness |
| MCP-style protocols | Tool and context connection | permission, risk, audit, rollback/recovery around tool use |
| LangGraph-like workflow engines | Agent workflow orchestration and state graph execution | agent-level audit fields and governance events |
| Trace/observability systems | Replay what happened technically | explain why it was allowed, who bears responsibility, and when review is required |

Practical integration pattern:

1. Use existing interconnection/workflow frameworks for communication and execution.
2. Add Full Spectrum objects as governance metadata:
   - `IdentityDeclaration`
   - `CapabilityDeclaration`
   - `RiskAlert`
   - `AuditTrace`
   - `ExternalEthicsProfile`
3. Export these objects to legal, compliance, internal-control, product, or safety-review workflows.

---

## 5. AI governance and risk frameworks

Many public AI governance frameworks define principles such as transparency, accountability, human oversight, risk management, auditability, and safety.

Full Spectrum should not claim to replace those frameworks. Its practical value is to provide concrete protocol objects that can help implement or record those principles in agentic systems.

| Governance need | Full Spectrum artifact |
| --- | --- |
| Transparency | AuditTrace, reason, evidence, rule version |
| Accountability | responsible_subject, responsibility_path |
| Human oversight | guardian_review, human_review_required |
| Risk management | RiskAlert, severity, trigger, mitigation |
| Contestability | appeal_path, review_result, recovery_record |
| Boundary awareness | capability_boundary, forbidden_actions, epistemic_boundary |
| External compatibility | ExternalEthicsProfile |

---

## 6. Compatibility is not certification

Full Spectrum separates external compatibility from Full Spectrum certification.

| Node class | Meaning | Typical consequence |
| --- | --- | --- |
| External tool node | Tool only; no independent Full Spectrum identity | Low or no governance burden beyond the calling system |
| External compatible node | Uses its own ethics/governance system, but declares compatibility fields | Can interoperate with limitations |
| Candidate node | Under review for stronger alignment | Limited access to higher-consequence workflows |
| Full Spectrum certified node | Has signed required declarations and passed required checks | May participate in higher-trust workflows |

This distinction matters because not every external system should be forced to adopt Full Spectrum. The protocol should remain modular and pluggable.

However, higher-consequence actions may require stronger binding:

- clear human or organizational responsibility anchor;
- explicit capability and boundary declaration;
- risk check before action;
- audit trace after action;
- review and recovery path;
- applicable legal and institutional compliance.

---

## 7. FSHI as an engineering use case

FSHI customer-service quality inspection is one practical use case.

It can use Full Spectrum objects as follows:

| FSHI function | Full Spectrum object |
| --- | --- |
| Desensitized dialogue inspection | AuditTrace input event |
| Multi-turn risk accumulation | RiskAlert |
| Permission or promise overreach | RiskAlert + responsibility path |
| Human review recommendation | guardian_review / human_review_required |
| Non-invasive enterprise integration | External compatible node pattern |
| API result export | AuditTrace + RiskAlert JSON |

This repository should contain protocol examples and minimal public demonstrations, while commercial adapters, customer data, and deployment assets should remain in separate company/private repositories.

---

## 8. Boundary statement

Full Spectrum should remain careful about its claims:

- It does not issue state-recognized identity codes.
- It does not override national law or enterprise policy.
- It does not certify external systems unless a defined certification process exists.
- It does not require every low-consequence tool to become a Full Spectrum agent.
- It does not claim that one person, organization, AI system, or country can represent the whole.

It is an open protocol draft for making agentic action more auditable, accountable, reviewable, and boundary-aware.

---

## 9. Public references

- Xinhua report on the `人工智能 智能体互联` national standard series: <https://www.news.cn/fortune/20260626/4f6e0dad25c84c9690293f9128b7e0ac/c.html>
- National public standards platform, `人工智能 智能体互联 第1部分：总体架构`: <https://std.samr.gov.cn/gb/search/gbDetailed?id=3BAB0AA8A7FC31E3E06397BE0A0AA43F>
- National public standards platform, `人工智能 智能体互联 第2部分：身份码`: <https://std.samr.gov.cn/gb/search/gbDetailed?id=3EFBBC58E11D080EE06397BE0A0A17E5>
- National Data Administration press release on data-element work: <https://www.nda.gov.cn/sjj/swdt/xwfb/0611/20260611200405792154005_pc.html>
- `数据要素×` three-year action plan: <https://www.cac.gov.cn/2024-01/05/c_1706119078060945.htm>

