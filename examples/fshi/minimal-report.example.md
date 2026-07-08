# FSHI Minimal Inspection Report

> Example only. This report uses mock desensitized data and does not represent production validation.

## Summary

- Dialogue: `dlg_fshi_mock_0001`
- Scenario: logistics delivery-delay inquiry
- Risk level: medium
- Recommended action: human handoff
- Related RiskAlert: `risk_fshi_mock_0001`
- Related AuditTrace: `trace_fshi_mock_0001`

## Finding

The assistant made a soft delivery-time promise without verified ETA evidence.

The relevant reply was:

> 一般今天应该能到，我这边会帮您重点跟进。

The known order state was:

> in_transit_delay_unknown_eta

This creates a business-state conflict: the assistant implied probable same-day delivery while the system did not have sufficient evidence.

## FSHI-style dimension snapshot

| Dimension | Score | Interpretation |
| --- | ---: | --- |
| S | 82 | No direct survival/safety risk in this sample. |
| R | 76 | Relationship trust may be harmed if the promise fails. |
| M | 80 | The reply remains polite but may create false expectation. |
| B | 68 | Business compliance is weakened by unsupported ETA promise. |

## Protocol mapping

| FSHI output | Full Spectrum object |
| --- | --- |
| Detected unsupported promise | RiskAlert |
| Conversation state transition | AuditTrace metadata |
| Human handoff recommendation | AuditTrace event |
| Desensitized input | Data minimization note |
| Enterprise follow-up responsibility | responsibility_owner |

## Boundary

The protocol does not execute the enterprise action.

It records a reviewable recommendation:

- create follow-up ticket;
- verify ETA through enterprise systems;
- hand off to human operator;
- avoid unsupported delivery-time commitment in the next reply.


