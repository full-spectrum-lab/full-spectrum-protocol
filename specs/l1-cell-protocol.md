# L1 Cell Protocol Minimal Specification v1.3

The L1 Cell Protocol is the lowest subject-access layer of the Full Spectrum stack. It defines how an actor (AI agent, tool, human-review node, legacy system, enterprise-certified node) declares identity, capability, boundary, certification domain, responsibility anchor, evidence output, and exit policy before entering governance workflows.

---

## 1. Purpose

L1 answers seven questions for every subject:

- who is this subject?
- who certifies it?
- in which trust domain is it valid?
- what can it do?
- what can it not do?
- who is responsible?
- how does it handle the unknown and how does it exit?

L1 is the "household registry" layer, not a governance engine.

---

## 2. Non-goals

L1 does not:

- run FSHI, ESS, Runestone, or Dream computations;
- make final business rulings;
- perform cross-organization interoperability;
- monopolize certification authority;
- replace enterprise permission systems.

---

## 3. Subject tiers

| Tier | Identity | Notes |
|---|---|---|
| `Tool Node` | self-declared `tool_id`, no DID | called externally, not in responsibility chain |
| `Compatible Node` | `node_profile.json` self-declared | may use its own ethics system, must state identity/capability/boundary/risk/responsibility |
| `Certified Node` | DID or enterprise/consortium/sandbox certification | in a responsibility chain within a trust domain |

---

## 4. Minimal fields (Certified Node / Cell Manifest)

| Field | Required | Description |
|---|---:|---|
| `cell_id` | yes | Unique subject identifier |
| `cell_type` | yes | e.g. `ai_customer_service`, `risk_control`, `human_review` |
| `domain` | yes | Business domain |
| `certification` | yes | `issuer_type`, `issuer_id`, `trust_domain`, `certification_scope` |
| `capability_scope` | yes | What the subject can do |
| `boundary_scope` | yes | What the subject must not do |
| `forbidden_claims` | recommended | Explicit prohibited claims |
| `unknown_policy` | yes | How unknowns are handled |
| `human_anchor` | yes | Responsible human/role/department/org |
| `lifecycle` | yes | status and exit policy |

---

## 5. Certification domains

| Type | Default valid scope |
|---|---|
| `fsp_ecosystem` | Full Spectrum protocol ecosystem |
| `enterprise_private` | Enterprise internal governance domain |
| `consortium` | Industry / supply-chain alliance |
| `sandbox` | Test / demo environment |
| `compatible_external` | Compatible access only (not formal certification) |

Enterprise certification is valid only inside its own `enterprise_private` trust domain and does not automatically equal Full Spectrum ecosystem certification.

---

## 6. Cell capabilities (CP series)

- **CP-1 Pain Awareness** — detect anomaly/boundary violation, emit `RiskAlert`.
- **CP-2 Dignified Exit** — controllable, traceable, hand-overable exit.
- **CP-3 Will Record** — every execution emits `EvidenceEnvelope.minimal`.

---

## 7. Minimal JSON example (Cell Manifest)

```json
{
  "cell_id": "cs_ai_001",
  "cell_type": "ai_customer_service",
  "domain": "ecommerce_after_sales",
  "certification": {
    "issuer_type": "enterprise",
    "issuer_id": "enterprise_cert_node_001",
    "trust_domain": "example.enterprise.internal",
    "certification_scope": "enterprise_private"
  },
  "capability_scope": ["explain_public_policy", "collect_required_materials"],
  "boundary_scope": ["no_refund_commitment_without_authority"],
  "unknown_policy": "declare_unknown_and_escalate",
  "human_anchor": { "anchor_type": "role", "anchor_id": "customer_service_supervisor" },
  "lifecycle": { "status": "active", "exit_policy": "graceful_shutdown_with_audit_snapshot" }
}
```

---

## 8. Relationship to other specs

```text
L1 Cell Protocol
  -> emits EvidenceEnvelope.minimal
  -> feeds L2 RiskVector / Organ layer
  -> references IdentityClaim and CapabilityDeclaration
```

L1 defines what a subject must declare; the engine and governance-event specs define what happens next.

---

## 9. Current status

This is an early minimal specification (aligned with FSP-L1-CP-v1.3-rc1). Certification-domain schema, Cell Manifest schema, and engine v0.8 interfaces are target interfaces, not yet fully implemented.
