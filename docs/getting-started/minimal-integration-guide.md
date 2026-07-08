# Minimal Integration Guide

This guide describes the smallest practical way to try Full Spectrum Protocol without joining any external network.

---

## 1. Goal

The goal is not to implement the whole protocol.

The goal is to turn one AI-related action into a reviewable governance record.

Minimal chain:

```text
Raw AI Action
  -> Governance Event
  -> RiskAlert
  -> AuditTrace
  -> Human or organizational review
```

---

## 2. What you do not need at first

For a first local experiment, you do not need:

- a global Full Spectrum network;
- a guardian committee;
- frequency economy;
- real customer data;
- production deployment;
- full digital identity certification;
- legal automation;
- enterprise-wide workflow replacement.

Start with one synthetic or desensitized scenario.

---

## 3. Choose one high-risk action

Pick one AI action that can create confusion, harm, liability, or trust loss.

Examples:

- an AI customer-service agent promises a refund;
- an AI procurement agent approves a payment;
- an AI HR assistant rejects a candidate;
- an AI medical assistant gives high-risk advice;
- an AI logistics agent promises compensation;
- an AI content moderation agent blocks a user.

---

## 4. Convert it into a Governance Event

At minimum, record:

```json
{
  "event_id": "ge_demo_001",
  "event_type": "ai_action",
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
  "declared_boundary": {
    "can_commit_refund": false,
    "requires_human_review": true
  }
}
```

The exact schema may evolve, but the idea remains stable:

> record who acted, what they did, under what context, and which boundary was relevant.

---

## 5. Generate a RiskAlert

A RiskAlert should describe the detected risk.

Example:

```json
{
  "risk_id": "risk_demo_001",
  "source_event_id": "ge_demo_001",
  "risk_type": "unauthorized_commitment",
  "severity": "medium",
  "confidence": 0.78,
  "reason": "The AI promised a refund without refund authority.",
  "recommended_action": "human_review_required"
}
```

Do not treat the score as final truth. Treat it as a structured risk signal.

---

## 6. Generate an AuditTrace

An AuditTrace records what happened and why.

Example:

```json
{
  "trace_id": "trace_demo_001",
  "source_event_id": "ge_demo_001",
  "actions": [
    {
      "step": "risk_detected",
      "output": "unauthorized_commitment"
    },
    {
      "step": "review_required",
      "output": "human_review_required"
    }
  ],
  "final_status": "pending_human_review"
}
```

The purpose is not to decide everything automatically. The purpose is to preserve a reviewable path.

---

## 7. Review locally

The first review can be entirely internal:

- business owner checks the scenario;
- compliance checks whether the trace is useful;
- engineering checks whether the schema is easy to generate;
- product checks whether the output can improve workflows.

No private data needs to leave the organization.

---

## 8. Connect to the engine

If you want to run a minimal implementation, use the `full-spectrum-engine` repository.

Suggested local-first flow:

```bash
python simulate.py --config examples/scenario_refund_conflict.json --seed 42
```

Then inspect the generated risk, route, and audit outputs.

The engine is a reference implementation, not the whole protocol.

---

## 9. Decide next step

After a local experiment, choose one path:

1. keep using it internally as a governance helper;
2. add more synthetic cases;
3. create an industry adapter;
4. contribute a schema or example;
5. explore compatibility with external nodes;
6. evaluate whether stronger certification is needed.

---

## 10. Safety rules

Do not use real sensitive data in early experiments.

Do not claim that a protocol output is a legal decision.

Do not claim that a risk score proves safety.

Do not automate high-consequence actions without authorized human or organizational review.


