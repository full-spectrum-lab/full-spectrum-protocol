# Three-Layer Evolution Path

This guide explains how Full Spectrum can be adopted without forcing every subject to join a global protocol network on day one.

The practical path has three layers:

1. internal engine layer;
2. cell protocol layer;
3. protocol network layer.

These layers are progressive. A subject can stop at layer 1 for a long time, remain useful at layer 2, and only move to layer 3 when cross-subject interaction becomes necessary.

---

## 1. Why the layers are separated

Many organizations do not want to begin with:

- a new public network;
- cross-organization registration;
- external governance dependencies;
- protocol-wide review responsibilities.

They usually want a much smaller starting point:

- solve one internal risk problem;
- keep data local;
- preserve existing business ownership;
- test whether governance signals are actually useful.

That is why Full Spectrum is not modeled as “join the whole network first.”  
It is modeled as a layered path from internal use to external coordination.

---

## 2. Layer 1: Internal Engine Layer

### Core question

How can one subject run Full Spectrum-compatible governance internally before joining any wider network?

### Typical carrier

- `full-spectrum-engine`

### Main function

The internal engine layer is a local-first runtime that can:

- ingest desensitized or synthetic business inputs;
- transform them into canonical governance context;
- evaluate risk;
- produce auditable outputs such as RiskAlert, AuditTrace, Runestone, or FSHI-style reports;
- support human review without replacing enterprise ownership.

### What it does not require

- no external node registration;
- no public identity certification;
- no guardian-network dependency;
- no global contribution accounting.

### Typical early use cases

- ecommerce customer-service over-commitment inspection;
- logistics customer-service dialogue quality review;
- internal multi-agent permission conflict review;
- cross-enterprise audit sample generation in a sandbox.

### Adoption signal

Layer 1 is successful when an organization can say:

> We ran the engine locally and it exposed risks or responsibility gaps that ordinary logging or QA did not make visible.

---

## 3. Layer 2: Cell Protocol Layer

### Core question

If a subject wants to become more legible and governable, what must it declare about itself before wider interaction?

### Main idea

The cell protocol layer is the minimal governance declaration layer for a subject.

It does not require a subject to expose all internal strategy or join a public network.  
It requires the subject to become structurally legible.

### Typical declarations

- identity claim;
- capability declaration;
- boundary statement;
- permission and revocation posture;
- responsibility path;
- recovery or circuit-break posture;
- local review and escalation path.

### Subject scope

A “cell” here does not only mean a single AI agent.

Depending on the scenario, a cell may be:

- an individual human operator;
- a single AI agent;
- an enterprise system;
- an organization unit;
- a city-scale service cluster;
- a state or industry-level subject.

The point is not size.  
The point is whether the subject can declare:

- who it is;
- what it can do;
- what it must not do;
- who carries the consequence if it acts.

### Relationship to node types

Node type and subject level are related but not identical.

- A small subject may still become a certified node.
- A large subject may remain only a compatibility node.
- An external tool may never become a certified Full Spectrum node at all.

For the current node-type framing, see:

- [Subject Levels and Node Types](./subject-levels-and-node-types.md)
- [External Node Guide](../../EXTERNAL_NODE_GUIDE.md)

### Adoption signal

Layer 2 is successful when a subject can say:

> Even if we do not join a wider protocol network yet, we can now express our identity, capability, boundary, and responsibility in a reusable governance format.

---

## 4. Layer 3: Protocol Network Layer

### Core question

What happens when multiple subjects need to coordinate across boundaries rather than only govern themselves internally?

### Main function

The protocol network layer adds cross-subject mechanisms such as:

- node registration;
- compatibility or certification status;
- cross-node audit exchange;
- shared review envelopes;
- ESS-style multi-path simulation interfaces;
- guardian-style review or conflict resolution paths;
- contribution records and ecosystem-level operating rules.

### Why this layer exists

Internal governance is not enough once interaction becomes external:

- one organization calls another organization’s agent;
- one system consumes another system’s output;
- one subject disputes another subject’s risk or authority declaration;
- a regulator, client, insurer, or public reviewer asks for a common audit envelope.

At that point, the problem is no longer only “is my system governable?”  
It becomes “how do we coordinate governance across boundaries without forcing everyone into one center?”

### What this layer should not become

The network layer should not become:

- a world government;
- a compulsory identity monopoly;
- a replacement for law or jurisdiction;
- a single point of moral interpretation.

Its job is narrower:

- make cross-subject interaction more legible;
- preserve reviewability;
- reduce responsibility ambiguity;
- create a shared envelope for risk and audit exchange.

### Adoption signal

Layer 3 is successful when multiple subjects can say:

> We kept our internal systems independent, but we can now exchange governance artifacts across boundaries in a structured and reviewable way.

---

## 5. Relationship between the three layers

```text
Internal Engine Layer
  -> local-first governance runtime
  -> solves one subject's own risk visibility problem

Cell Protocol Layer
  -> makes the subject legible
  -> declares identity, capability, boundary, and responsibility

Protocol Network Layer
  -> coordinates multiple subjects
  -> exchanges audit, risk, and review artifacts across boundaries
```

This is not a forced staircase.  
Different subjects may remain at different layers for long periods.

Examples:

- A small company may stay at Layer 1 only.
- A regulated enterprise may use Layer 1 + Layer 2 for a long time.
- A multi-organization ecosystem may need all three.

---

## 6. What this means for repository boundaries

The layered path also clarifies repository roles:

| Repository | Main role | Closest layer |
| --- | --- | --- |
| `full-spectrum-engine` | local-first runtime and minimal governance execution | Layer 1 |
| `full-spectrum-enterprise-governance` | enterprise-facing cases, adapters, review workflows | Layer 1 + Layer 2 |
| `full-spectrum-protocol` | schemas, RFCs, node types, cross-subject governance semantics | Layer 2 + Layer 3 |
| `full-spectrum-commons` | ecosystem maps, visual orientation, public indexes | all layers |

---

## 7. Recommended reading order

If you are exploring this layered path for the first time:

1. [START_HERE.md](../../START_HERE.md)
2. [Subject Levels and Node Types](./subject-levels-and-node-types.md)
3. [External Node Guide](../../EXTERNAL_NODE_GUIDE.md)
4. [full-spectrum-engine](https://github.com/full-spectrum-lab/full-spectrum-engine)
5. [full-spectrum-enterprise-governance](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance)
6. [RFC 0001: Full Spectrum Protocol](../../rfcs/0001-full-spectrum-protocol.md)

---

## 8. Short version

Full Spectrum should not begin by asking everyone to join a network.

It should begin by letting a subject:

1. run a local engine;
2. declare itself as a governed cell;
3. join wider coordination only when external interaction actually requires it.

That is the practical meaning of the three-layer evolution path.
