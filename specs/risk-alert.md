# RiskAlert Minimal Specification v0.1

RiskAlert is the minimal object used to describe a detected or suspected risk in a reviewable AI-related interaction.

---

## 1. Purpose

RiskAlert records enough information to ask:

- what risk was detected;
- who or what detected it;
- who may be affected;
- how severe and urgent it is;
- how confident the detector is;
- what review or mitigation is recommended.

RiskAlert does not execute the recommended action. It records a risk signal and a recommended next step.

---

## 2. Non-goals

RiskAlert does not:

- prove that harm has occurred;
- decide legal liability;
- replace enterprise review;
- replace human review in high-consequence contexts;
- certify a model, agent, organization, or workflow;
- require joining a Full Spectrum network.

---

## 3. Minimal fields

| Field | Required | Description |
|---|---:|---|
| `risk_id` | yes | Stable identifier for this risk alert |
| `created_at` | yes | Creation time |
| `detector_id` | yes | System, subject, or node that detected the risk |
| `affected_subject_id` | yes | Subject primarily affected by the risk |
| `risk_dimension` | yes | Risk type such as permission boundary, state conflict, privacy, or responsibility gap |
| `severity` | yes | `low`, `medium`, `high`, or `critical` |
| `confidence` | yes | Detector confidence from 0 to 1 |
| `urgency` | yes | Response urgency |
| `summary` | yes | Human-readable risk summary |
| `recommended_action` | yes | Recommended review or mitigation action |

---

## 4. Relationship to GovernanceEvent

RiskAlert is usually generated from one or more Governance Events.

```text
GovernanceEvent -> RiskAlert
```

`GovernanceEvent` records what happened. `RiskAlert` interprets why the event may require review.

---

## 5. Relationship to AuditTrace

RiskAlert should be linked into an AuditTrace when the risk is reviewed, escalated, disputed, mitigated, or closed.

```text
RiskAlert -> AuditTrace
```

The `related_trace_id` field may reference the AuditTrace.

---

## 6. Recommended actions

RiskAlert may recommend:

- continue with logging;
- request human review;
- request ESS simulation;
- request guardian review;
- downgrade;
- pause;
- human handoff;
- circuit break;
- recover;
- close with no action.

These are recommendations unless a separate enterprise workflow explicitly authorizes execution.

---

## 7. Machine-readable schema

Schema:

- [`schemas/risk-alert.schema.json`](../schemas/risk-alert.schema.json)

Sample:

- [`examples/fshi/api-contract/risk-alert.sample.json`](../examples/fshi/api-contract/risk-alert.sample.json)

---

## 8. Boundary

RiskAlert should preserve uncertainty. A low-confidence alert should not be presented as fact.

If the detector lacks enough evidence, the alert should record uncertainty rather than inventing certainty. This is part of boundary self-knowledge.

