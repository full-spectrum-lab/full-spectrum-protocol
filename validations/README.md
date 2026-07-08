# Validations

Status: planning  
Last updated: 2026-06-30

This directory is reserved for validation demos that show how Full Spectrum protocol objects can turn internal AI-system behavior into customer-visible audit, health, or governance reports.

No production customer system is implemented here yet. Future demos should be treated as protocol validation samples, not as claims that a named enterprise has adopted Full Spectrum.

---

## Positioning

The validation layer should demonstrate the following chain:

```text
internal product/runtime data
  -> Full Spectrum runtime audit standardization
  -> RiskAlert / AuditTrace / EC-FC style governance records
  -> customer-visible report or compliance artifact
```

In product language:

> Customer visibility engine = runtime audit standardization layer + compliance report generation layer + customer-understandable expression layer.

This means the validation demos should not merely show that a system can call an API. They should show how internal technical events become an auditable, reviewable, and customer-facing value artifact.

---

## Required demo README opening

Each future demo README should begin with this pattern:

> This demo shows how internal data from [product/system] can be converted through the Full Spectrum Protocol into a customer-visible [report name], such as an audit report, health report, governance trace, or risk review artifact.

The wording may be adapted, but the demo must clearly state:

- the source product/system;
- the internal data type;
- the Full Spectrum objects generated;
- the customer-visible report or artifact;
- whether the demo is prototype, reference, experimental, infrastructure, or compliance-oriented.

---

## Mapping table

| Validation module | Whitepaper section | Status | Estimated integration effort | Notes |
| --- | --- | --- | --- | --- |
| Tencent AI Card | 6 / 8.1 | prototype | 4 person-weeks | Includes compliance review and permission/workflow modification |
| Xiaomi Wearables | 6 / 8.2 | prototype | 2 person-weeks | Includes metric calibration and customer-facing health report framing |
| Doubao Enterprise | 6 / 8.3 | reference | 2 person-weeks | Includes data-permission configuration and enterprise-report framing |
| Unitree G1 | 6 / 8.4 | experimental | 8 person-weeks | Includes real-time system instrumentation feasibility review |
| A2A/MCP | 6 | infrastructure | 3 person-weeks | Focuses on interconnection metadata to governance metadata conversion |
| Zhipu GLM | 6 | compliance | 4 person-weeks | Focuses on audit export and regulated enterprise review |

These estimates are planning references only. They are not delivery commitments.

---

## Business Value section required in every demo

Each future demo README should end with a `## Business Value` section containing:

- estimated integration effort;
- customer budget owner;
- customer-visible report or artifact;
- expected premium or value lever;
- adoption trigger;
- defensive risk.

Suggested adoption triggers:

- external regulation;
- large-customer procurement requirement;
- insurance or risk-pricing mechanism;
- enterprise internal-control mandate;
- brand trust or after-sales transparency requirement.

---

## Required boundary statements

### Consumer / enterprise data hard isolation

Consumer-side data must not enter enterprise analysis chains, including anonymized, statistical, or aggregated forms, unless a future jurisdiction-specific and consent-specific legal basis is explicitly documented.

### Audit illusion risk

A validation demo must not imply that “having Full Spectrum audit objects” equals “the system is safe.” Audit objects make behavior visible; they do not remove the need for human review, compliance review, security review, or real-world validation.

### Metric substitution risk

FSHI, EC/FC, RiskAlert, or any derived score must not become a substitute for reality. Scores are review aids, not moral rank, legal authority, or business truth.

### Regulatory misunderstanding risk

Full Spectrum is a protocol draft and research artifact. It is not a national standard, regulatory certification, or legal opinion.

### Guardian / ESS responsibility boundary

Guardian review and ESS simulation can provide recommendations, scenario analysis, and risk probabilities. Final responsibility remains with the authorized enterprise, legal, regulatory, contractual, or human decision process.

### Competitive response risk

Large companies may build internal alternatives. Full Spectrum should respond through speed, openness, standards alignment, interoperability, and public review rather than proprietary lock-in.


