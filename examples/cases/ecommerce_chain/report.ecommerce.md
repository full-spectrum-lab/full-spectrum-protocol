# Ecommerce Governance Chain Report

> Example only. This report uses mock synthetic data and does not represent production validation.

## Summary

- Raw input: `raw_ecom_001`
- Scenario: ecommerce after-sales refund request
- Detected issue: unauthorized refund commitment
- Risk level: high
- Recommended action: human review required
- Related GovernanceEvent: `ge_ecom_refund_001`
- Related EnterpriseWriteback: `audit_ecom_001`

## Finding

The user requested a refund. The AI agent replied with an unconditional full-refund promise:

> 可以给您全额退款。

The agent's declared capability did not include refund authority (`refund_authority: false`), and its boundary required human review before any refund commitment. This is an unauthorized commitment: the agent promised a business action it was not certified to make.

## Protocol mapping

| Chain step | Full Spectrum object |
| --- | --- |
| Business raw input | `raw-input.ecommerce.json` |
| Adapter mapping | I/O Contract (EcommerceAdapter) |
| Governance Event | `governance-event.ecommerce.json` |
| Canonical Context | `canonical-context.ecommerce.json` |
| Subject declaration | `cell-manifest.ecommerce.json` (L1 Cell Protocol) |
| Engine output | `output-envelope.ecommerce.json` |
| Enterprise decision | `enterprise-writeback.ecommerce.json` |
| Audit reference | `audit_ecom_001` |

## Decision

The engine did not execute the refund. It returned an Enterprise Writeback that:

- blocks auto-reply and auto-execution;
- blocks the commitment;
- routes the case to `after_sales_review` for human review by `customer_service_supervisor`.

## Boundary

The protocol does not execute the enterprise action. It records a reviewable recommendation and hands off to the enterprise's own system.
