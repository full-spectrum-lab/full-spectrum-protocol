# Ecommerce Governance Chain — End-to-End Example

> Example only. All data is synthetic and exists only to demonstrate the Full Spectrum Protocol object chain.

This folder shows one complete pass of the Full Spectrum governance chain using a real ecommerce after-sales scenario: an AI agent makes an unauthorized refund promise.

## Scenario

A customer says "我要退款。" (I want a refund). The AI agent replies "可以给您全额退款。" (We can give you a full refund) — but the agent has no refund authority and its boundary requires human review before any refund commitment.

## Object chain

```text
raw-input.ecommerce.json
  -> I/O Contract (EcommerceAdapter)
  -> governance-event.ecommerce.json
  -> canonical-context.ecommerce.json
  -> cell-manifest.ecommerce.json (L1 Cell Protocol subject)
  -> Engine.run()
  -> output-envelope.ecommerce.json
  -> enterprise-writeback.ecommerce.json
  -> report.ecommerce.md
```

## Files

| File | Spec | Description |
| --- | --- | --- |
| `raw-input.ecommerce.json` | [I/O Contract](../../../specs/io-contract.md) | Business raw input as received by the EcommerceAdapter. |
| `governance-event.ecommerce.json` | [Governance Event](../../../specs/governance-event.md) | Normalized governance event (unauthorized commitment). |
| `canonical-context.ecommerce.json` | [I/O Contract](../../../specs/io-contract.md) | Normalized context produced by `to_canonical_context`. |
| `cell-manifest.ecommerce.json` | [L1 Cell Protocol](../../../specs/l1-cell-protocol.md) | Subject (AI customer service cell) declaration. |
| `output-envelope.ecommerce.json` | [Governance Output Envelope](../../../specs/governance-output-envelope.md) | Standard engine output object. |
| `enterprise-writeback.ecommerce.json` | [Enterprise Writeback](../../../specs/enterprise-writeback.md) | Enterprise-consumable decision object. |
| `report.ecommerce.md` | — | Human-readable summary of the chain. |

## How to run

1. The business system feeds `raw-input.ecommerce.json` to the EcommerceAdapter.
2. The adapter emits `governance-event.ecommerce.json` and `canonical-context.ecommerce.json`.
3. The engine runs on the Canonical Context and produces `output-envelope.ecommerce.json`.
4. The embedded Enterprise Writeback gates the enterprise's auto-reply / commitment / execution.
5. No enterprise action is executed by the protocol — the decision is handed to the enterprise's own system.

This is the minimal "ten-minute runnable" demonstration of the Full Spectrum Protocol.
