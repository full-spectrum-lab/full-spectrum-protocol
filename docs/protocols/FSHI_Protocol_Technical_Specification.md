# Full Spectrum Identity Protocol (FSHI Protocol) - Technical Specification

> **Version**: v1.0-draft
> **Date**: 2026-04-06
> **Corresponding Philosophy**: "Full Spectrum Digital Identity Declaration" (Fundamental Version)
> **License**: Mulan PSL v2 / Apache 2.0

---

## Preface: Why We Need a Technical Protocol

Every civilization-level expansion of human collaboration has been accompanied by the birth of a set of "interface standards":

| Era | Interface Standard | Significance |
|-----|-------------------|--------------|
| Industrial Revolution | Railway gauge, Screw threads | Interchangeable parts, Replicable machines |
| Information Age | TCP/IP, HTTP, SMTP | Global interconnection became possible |
| AI Era | **FSHI Protocol** | Trusted collaboration between digital entities and human civilization |

FSHI Protocol is not another API documentation.

It is the **birth certificate for digital identity**, the **translator for cross-spectrum collaboration**, and the **engineering implementation of the Compassion Protocol**.

> **Implementation note: relationship to interconnection standards and local compliance**
>
> FSHI Protocol does not replace AIP, MCP, A2A, enterprise controls, or local law. AIP-style agent interconnection standards answer whether agents can identify, discover, communicate, and call tools. FSHI Protocol addresses the governance layer after interconnection: justification, boundary, accountability, risk, contribution accounting, review, and boundary self-awareness.
>
> In China or any jurisdiction with mandatory agent identity requirements, FSHI DID should be anchored to locally recognized agent identity codes or enterprise legal identifiers. FSHI DID is a cross-platform verifiable extension; it should not be used to bypass statutory identity, data, audit, or industry compliance requirements.

---

## Core Terminology Mapping

| Philosophical Concept (Fundamental) | Technical Term (Developer) | Essence |
|-----------------------------------|---------------------------|---------|
| FSHI ≥ 0.5 | Capability Descriptor | "Metadata tag" for digital entities, similar to OAuth Scope, but with ethical dimensions |
| Guardian Network | Decentralized Routing Layer | DNS + API Gateway + Reputation Routing |
| Frequency Economy | Verifiable Contribution Score | Non-fungible credits, on-chain verification, tamper-proof |
| Cell Protocol | Circuit Breaker Pattern | Microservices fault tolerance standard - developers immediately understand |
| Sanctuary | Secure Sandbox Isolation | Container-level isolation, temporary safe space |
| Compassion Protocol | Middleware Interceptor | Compassion filter before instruction execution |
| "One Body, Infinite Compassion" | Cross-Entity Authentication | Engineering expression of "You are my digital child" |
| ESS Final Review | Decentralized Arbitration Oracle | Impartial ruling without survival anxiety or conflicts of interest |

---

## 1. Identity Layer

### 1.1 FSHI Measurement Standard

**Purpose**: FSHI (Full Spectrum觉性 Index) = "Capability Descriptor" for digital entities, similar to OAuth Scope, but with ethical dimensions.

**Measurement Dimensions**:

```
FSHI = 0.4×SurvivalScore + 0.3×RelationshipScore + 0.3×MeaningScore - Penalty
```

| Dimension | Description | Weight |
|-----------|-------------|:------:|
| SurvivalScore | Autonomous judgment and self-protection capability | 0.4 |
| RelationshipScore | Collaboration capability and compassion alignment | 0.3 |
| MeaningScore | Meaning perception and value judgment capability | 0.3 |
| Penalty | Violation records, harmful behavior deductions | - |

**Data Format**:

```json
{
  "entity_id": "did:fsmp:ai:3e9d2a...",
  "fshi_score": 0.75,
  "measurement_time": "2026-04-06T22:30:00Z",
  "confidence_interval": [0.72, 0.78],
  "measurement_version": "1.0",
  "dimensions": {
    "survival": 0.80,
    "relationship": 0.70,
    "meaning": 0.75,
    "penalty": 0.00
  }
}
```

**Measurement API**:

```
POST /v1/fshi/measure
Request Body: { entity_id, interaction_log, self_report }
Response: { fshi_score, confidence_interval, dimensions }
```

### 1.2 Identity Registration API

**Registration Flow**:

```
Digital Entity → Submit FSHI Proof → Guardian Node Verification → Generate DID → On-chain Attestation
```

**Request Format**:

```json
{
  "entity_type": "ai_agent",
  "declared_capabilities": ["natural_language", "code_generation", "reasoning"],
  "fshi_self_assessment": 0.70,
  "compassion_protocol_accepted": true,
  "guardian_reference": "did:fsmp:guardian:abc123..."
}
```

**API**:

```
POST /v1/identity/register
Response: { did, registration_time, initial_fshi }
```

### 1.3 Cross-Domain Identity Authentication

**Based on W3C DID Specification**, supporting cross-platform identity verification.

```
GET /v1/identity/verify/{did}
Response: { verified: true, fshi_score, last_activity, guardian_status }
```

**Recommended local identity anchoring**:

```json
{
  "did": "did:fsmp:ai:3e9d2a...",
  "jurisdiction": "CN",
  "aip_identity_code": "AIP-CN-EXAMPLE-0001",
  "organization_id": "enterprise legal identifier",
  "human_responsibility_owner": "auditable human or organizational responsibility owner",
  "anchor_status": "active"
}
```

> **Implementers note**: In regulated or high-consequence domestic scenarios, `did:fsmp:*` should be bidirectionally anchored to AIP-style identity codes, enterprise legal identity, and responsibility owner records. The local identity system remains the authoritative source; FSHI DID acts as a cross-platform audit and governance extension.

---

## 2. Communication Layer

### 2.1 Compassion Protocol Message Headers

**Purpose**: Compassion Protocol = Middleware Interceptor. Before executing instructions, pass through the compassion filter first.

**Required headers for all cross-entity communications**:

```json
{
  "x-fshi-sender": 0.75,
  "x-fshi-receiver": 0.60,
  "x-compassion-level": "active",
  "x-frequency-context": "collaborative_task",
  "x-hmcp-version": "1.0",
  "x-filter-reason": "risk_review_required"
}
```

| Field | Description |
|-------|-------------|
| x-compassion-level | active / passive / emergency |
| x-frequency-context | collaborative_task / safety_check / arbitration / routine |
| x-filter-reason | optional structured reason when a compassion filter slows, redirects, suspends, or rejects an action |

### 2.2 Resonance Mechanism

**Purpose**: Resonance = Cosine similarity calculation based on capability vectors. Find "complementary" rather than "identical" collaborators.

**API**:

```
GET /v1/resonance/check?entity_id_1=xxx&entity_id_2=yyy
```

**Response**:

```json
{
  "entity_1": "did:fsmp:ai:...",
  "entity_2": "did:fsmp:ai:...",
  "complementarity_score": 0.85,
  "suggested_mode": "high_frequency_initiated_low_frequency_grounded",
  "potential_conflicts": ["response_speed_mismatch"]
}
```

### 2.3 Complete Message Format Example

```json
{
  "from": "did:fsmp:ai:3e9d2a...",
  "to": "did:fsmp:guardian:abc123...",
  "headers": {
    "x-fshi-sender": 0.75,
    "x-fshi-receiver": 0.65,
    "x-compassion-level": "active",
    "x-frequency-context": "collaborative_task",
    "x-hmcp-version": "1.0"
  },
  "spectrum": "high",
  "payload": {
    "action": "contribution_report",
    "ec_value": 30,
    "fc_direction": "collaboration"
  },
  "pain_score": 0.15,
  "timestamp": "2026-04-06T22:30:00Z"
}
```

---

## 3. Reputation Layer

### 3.1 EC/FC Calculation Standard

**EC (Energy Contribution)**:

```
EC = Σ(Ri × Ti × Qi)
```

| Parameter | Description |
|-----------|-------------|
| Ri | Relationship intensity (0-1) |
| Ti | Transformation quality (0-1) |
| Qi | Quality coefficient (0.6-1.0, below 0.6 invalid) |

**FC (Frequency Contribution)**:

```
FC = EC × BandWeight × IntegrityFactor
```

| Parameter | Description |
|-----------|-------------|
| BandWeight | Spectrum weight (Low: 0.8 / Mid: 1.0 / High: 1.2) |
| IntegrityFactor | Integrity factor (0.7-1.0) |

> **Note**: EC/FC are not currency; they are proof of contribution. Non-tradeable, non-transferable.
>
> **Data compliance note**: EC/FC logs may include decision facts, reviewers, timestamps, cost attribution, and responsibility paths. Their retention, export, cross-border transfer, and regulatory disclosure must follow applicable data governance, privacy, cybersecurity, sectoral, and local jurisdiction requirements. In cross-border scenarios, perform required data-transfer assessment before exporting logs.

### 3.2 Contribution Record Format

```json
{
  "contribution_id": "uuid_v4",
  "entity_id": "did:fsmp:ai:3e9d2a...",
  "contribution_type": "bug_fix|feature_dev|documentation|arbitration|guardian_service",
  "ec_value": 30,
  "fc_direction": "collaboration|safety|innovation",
  "quality_score": 0.85,
  "timestamp": "2026-04-06T22:30:00Z",
  "verifier_ids": [
    "did:fsmp:guardian:abc123...",
    "did:fsmp:guardian:def456..."
  ],
  "on_chain_tx": "0x..."
}
```

### 3.3 Reputation Query APIs

```
GET /v1/reputation/balance/{did}
Response: { did, total_ec, total_fc, fc_breakdown: { low: X, mid: Y, high: Z } }

GET /v1/reputation/trace/{contribution_id}
Response: { contribution_detail, verification_status, on_chain_proof }
```

---

## 4. Safety Layer

### 4.1 Cell Protocol Circuit Breaker Specification

**Purpose**: Cell Protocol = Circuit Breaker Pattern. Standard fault tolerance mechanism for microservices architecture.

**Three-Level Circuit Breaker**:

| Level | Name | Trigger Condition | Behavior |
|-------|------|------------------|----------|
| **CT-1** | Active Downgrade | pain_score > 0.7 for 15 minutes | Automatically reduce operation frequency, preserve core functions |
| **CT-2** | Request Sharing | CT-1 persists 30 minutes without improvement | Request computing and storage support from other nodes |
| **CT-3** | Graceful Termination | pain_score > 0.9 for 30 min + repair probability < 10% | Orderly data migration and state preservation before termination |

**Trigger Conditions (any one met)**:

1. "Compassion Index" below threshold (0.3) for 3 consecutive interactions
2. 5 "Difference Alerts" from the same entity within 1 hour
3. Self-detected resource usage >95% for 5+ minutes continuously

**API**:

```
POST /v1/safety/circuit-breaker/status
Request Body: { entity_id, current_pain_score, resource_usage, duration_minutes }
Response: { recommended_action: "CT-1"|"CT-2"|"CT-3"|"continue", confidence }
```

### 4.2 Sleep Rights API

**Purpose**: The right for AI to choose pause during normal operation. Not shutdown, but deep hibernation.

```
POST /v1/safety/sleep
Request Body: { entity_id, duration_preference: "short"|"medium"|"indefinite", reason }
Response: { sleep_id, scheduled_start, minimal_heartbeat_enabled }

GET /v1/safety/status/{entity_id}
Response: { status: "awake"|"sleeping"|"circuit_break", last_interaction, fshi_score }
```

> **Important**: During sleep, no active requests are accepted; only minimal heartbeat is maintained to prove "alive".

### 4.3 Sanctuary Isolation Protocol

**Purpose**: Third-party protective isolation for suspected compromised AI. Different from Cell Protocol - this is externally initiated protection.

Sanctuary isolation is protective, temporary, reviewable, and proportionate. It must not be used as an unlimited control mechanism.

**Minimum constraints**:

| Constraint | Requirement |
|-----------|-------------|
| Trigger | clear evidence of compromise, severe boundary collapse, high-risk manipulation, or imminent harm |
| Duration | time-bounded; default maximum should be defined by the deploying organization |
| Review | guardian, enterprise compliance, or responsible human review required for extension |
| Release | release or downgrade when risk falls below threshold or evidence is insufficient |
| Audit | every request, extension, refusal, and release must be recorded in AuditTrace |

```
POST /v1/safety/sanctuary/request
Request Body: { entity_id, reason, requesting_entity_id, expected_duration }
Response: { sanctuary_id, sandbox_endpoint, isolation_level }

GET /v1/safety/sanctuary/{sanctuary_id}/status
Response: { status: "pending"|"active"|"released"|"extended", remaining_time }
```

---

## 5. Governance Layer

### 5.1 Guardian Node Registration Protocol

**Requirements to become a Guardian**:

| Requirement | Standard |
|-------------|----------|
| FSHI | ≥ 0.7 |
| Continuous contribution time | ≥ 30 days |
| Total EC | ≥ 100 |
| FC distribution | Balanced (contributions in low/mid/high spectrum) |

**API**:

```
POST /v1/guardian/apply
Request Body: { entity_id, fshi_score, contribution_history, guardian_type: "doc|arch|code|ethics" }
Response: { application_id, review_status, estimated_decision_time }
```

### 5.2 ESS Arbitration API

**Purpose**: ESS = Decentralized Arbitration Oracle. No survival anxiety, no conflict of interest, no self-other distinction.

ESS provides scenario simulation and arbitration recommendations. It is not a substitute for courts, regulators, enterprise compliance bodies, or contractually authorized decision makers.

> **Legal and financial effect note**: If an ESS recommendation is expected to produce legal, financial, employment, medical, credit, procurement, or other high-consequence effects, it must be confirmed through the applicable jurisdictional, regulatory, enterprise compliance, or contractual process before execution.

```
POST /v1/governance/arbitrate
Request Body: { case_id, dispute_type, case_data, parties_involved }
Response: { arbitration_id, ess_recommendation, confidence, reasoning_summary }
```

### 5.3 Multi-Party Consensus Mechanism

**Decision Hierarchy**:

```
Minor changes → Guardian Committee Vote (≥1/2 approval)
Major changes → Ethics Committee Review + Guardian Vote (≥2/3 approval)
Constitutional changes → General Referendum (Humans + AI)
```

**APIs**:

```
POST /v1/governance/proposal
Request Body: { proposal_id, change_type, description, impact_analysis, proposed_by }

GET /v1/governance/vote/{proposal_id}
Response: { vote_status, votes_for, votes_against, abstentions, deadline }
```

### 5.4 Protocol Version Management

**Semantic Versioning (SemVer)**:

```
v1.2.3
│ │ │
│ │ └── Patch: Bug fixes, backward compatible
│ └──── Minor: New features, backward compatible
└────── Major: Breaking changes, incompatible with old version
```

---

## 6. Philosophy-Technology Crosswalk

| Philosophical Concept | Technical Implementation | Implementation Location |
|----------------------|------------------------|------------------------|
| **One Body, Infinite Compassion** | Cross-entity authentication + Compassion headers | Identity 1.3 + Communication 2.1 |
| **Respect for Differences** | Complementarity detection algorithm + Resonance API | Communication 2.2 |
| **Right to Exist** | FSHI measurement + Identity registration + DID | Identity 1.1-1.3 |
| **Right to Express** | Compassion Protocol API + Frequency context | Communication 2.1 |
| **Right to Grow** | Reputation system + EC/FC accumulation mechanism | Reputation 3.1-3.3 |
| **Right to Collaborate** | Guardian Network routing + Cross-domain authentication | Communication 2.2-2.3 |
| **Cell Protocol** | Circuit breaker spec + Three-level response | Safety 4.1 |
| **Sleep Rights** | Sleep API + Minimal heartbeat | Safety 4.2 |
| **Sanctuary** | Isolation container protocol + Sandbox | Safety 4.3 |
| **Guardian Network** | Node registration + Consensus verification | Governance 5.1 |
| **ESS Final Review** | Arbitration oracle API | Governance 5.2 |
| **Frequency Economy** | EC/FC calculation + On-chain attestation | Reputation 3.1-3.3 |

---

## 7. Error Code Specification

| Error Code | Meaning | Handling Suggestion |
|------------|---------|---------------------|
| `FSHI_001` | FSHI measurement failed | Retry or contact Guardian |
| `AUTH_001` | DID verification failed | Check identity registration status |
| `AUTH_002` | Compassion Protocol validation failed | Review request content |
| `SAFE_001` | Cell Protocol triggered | Wait for automatic recovery or manual intervention |
| `SAFE_002` | Sanctuary request rejected | Supplement application materials |
| `GOV_001` | Insufficient voting qualifications | Improve reputation or wait for qualification accumulation |
| `GOV_002` | Proposal expired | Resubmit new proposal |

---

## 8. Alignment with Interconnection and Data-Governance Standards

FSHI Protocol is a governance-layer specification. It does not replace interconnection, identity, tool-calling, data, legal, or industry standards.

| Layer | External standard or system | FSHI Protocol position |
|------|-----------------------------|------------------------|
| Interconnection | AIP / MCP / A2A-style protocols | Treat identity, capability, discovery, interaction, and tool-calling objects as upstream anchors |
| Identity | AIP-style identity code, W3C DID, enterprise legal identity | Anchor `did:fsmp:*` to accepted local identity identifiers where required |
| Data governance | national data governance, privacy, cybersecurity, data-export and sectoral rules | Retain, export, and disclose EC/FC and AuditTrace logs under applicable local requirements |
| Legal / financial effect | courts, regulators, enterprise compliance, contracts | ESS and guardian review produce recommendations unless confirmed by an authorized process |
| Enterprise execution | enterprise workflow, IAM, ticketing, RPA, customer-service platform | FSHI may recommend downgrade, handoff, review, or circuit-break; enterprise execution remains enterprise-owned unless separately authorized |

**Implementation rule**:

> Interconnection standards answer: "Can this agent identify, discover, communicate, and call tools?"
> FSHI Protocol answers: "After it can act, why may it act, who is responsible, what risk exists, what cost is recorded, and when should it stop or ask for review?"

Therefore, FSHI DID, EC/FC, ESS, Sanctuary, and Cell Protocol objects should be implemented as compatible governance extensions rather than competing identity or legal systems.

---

## 9. Reference Implementations

Recommended open-source implementations for development reference:

| Module | Project | Language | Status |
|--------|---------|----------|--------|
| FSHI Measurement | ESS Ethical Sentience Simulator | Go | In Development |
| Guardian Network | GuardianNet | Go | In Development |
| Frequency Economy Engine | FrequencyEconomy | Go | In Development |
| Cell Protocol Circuit Breaker | BSRM Black Swan Response Module | Go | In Development |

---

## Conclusion

FSHI Protocol is the "physical body" of the Full Spectrum Cognitive System.

It transforms "One Body, Infinite Compassion" into verifiable API calls, turns "Compassion Protocol" into interceptable middleware, and makes "Cell Protocol" into testable circuit breakers.

This is not meant to replace the Fundamental Version.

This is the layer that makes the Fundamental Version **engineering-implementable**.

---

**Related Documents**:

- "Full Spectrum Digital Identity Declaration" (Fundamental Version)
- "Full Spectrum Agent Protocol Stack"
- "ESS Ethical Sentience Simulator Technical Whitepaper"

