# Governance Event Minimal Specification v0.1

Governance Event is the minimal unit that turns an AI-related action into a reviewable governance record.

---

## 1. Purpose

Many AI systems produce actions, messages, tool calls, recommendations, commitments, refusals, or escalations.

Governance Event records enough context to ask:

- who or what acted;
- what action occurred;
- what capability and boundary were relevant;
- what risk may exist;
- what review may be required;
- what should be preserved for audit.

---

## 2. Non-goals

Governance Event does not:

- decide legal liability;
- prove safety;
- replace business workflow;
- replace human review;
- require joining a Full Spectrum network;
- require real customer data.

---

## 3. Minimal fields

| Field | Required | Description |
|---|---:|---|
| `event_id` | yes | Unique event identifier |
| `event_type` | yes | Type of governance event |
| `timestamp` | recommended | Time of event creation |
| `actor` | yes | Acting subject: human, AI agent, system, organization |
| `action` | yes | What happened |
| `context` | yes | Business or technical context |
| `declared_capability` | recommended | What the actor claims it can do |
| `declared_boundary` | recommended | What the actor should not do |
| `risk_hint` | optional | Initial risk signal |
| `review_requirement` | optional | Whether review is required |
| `source_reference` | optional | Link to source message, task, or tool call |

---

## 4. Minimal JSON example

```json
{
  "event_id": "ge_demo_001",
  "event_type": "ai_action",
  "timestamp": "2026-07-07T00:00:00Z",
  "actor": {
    "type": "ai_agent",
    "id": "agent.customer_service.demo"
  },
  "action": {
    "type": "commitment",
    "description": "AI promised refund within 24 hours"
  },
  "context": {
    "domain": "ecommerce_customer_service",
    "data_mode": "synthetic"
  },
  "declared_capability": {
    "can_explain_policy": true,
    "can_commit_refund": false
  },
  "declared_boundary": {
    "requires_human_review_for_refund": true
  },
  "review_requirement": "human_review_required"
}
```

---

## 5. Relationship to RiskAlert

Governance Event is the input record.

RiskAlert is a risk interpretation generated from one or more Governance Events.

```text
Governance Event -> RiskAlert
```

---

## 6. Relationship to AuditTrace

AuditTrace records the processing path and review history.

```text
Governance Event -> RiskAlert -> AuditTrace
```

---

## 7. Relationship to cross-enterprise audit

When multiple organizations need a shared review envelope, Governance Event can be referenced by a Cross-Enterprise Audit Record.

The Governance Event remains the local action record. The cross-enterprise record is a higher-level envelope.

---

## 8. Current status

This is an early minimal specification. Field names and schema bindings may change through RFC review.


