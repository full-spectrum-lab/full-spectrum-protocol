# Roadmap

This roadmap describes how the Full Spectrum Ethics Protocol Stack may evolve from a document collection into a verifiable open protocol.

## Phase 0: Public entry repair

Status: largely complete.

- Fix README encoding and public entry.
- Add Chinese and English entry documents.
- Add START_HERE, ROADMAP, GOVERNANCE.
- Clarify the relationship between protocol, use case, and product.
- Clarify the relationship between Full Spectrum, AIP-style agent interconnection standards, A2A/MCP-style ecosystems, and data-governance trends.
- Add a machine-readable entry document for agents and agent frameworks.
- Add minimal GovernanceEvent specification and validation sample.

## Phase 1: Protocol consolidation

Goal: make the protocol readable and reviewable.

- Publish a concise Full Spectrum Protocol Outline.
- Create a glossary.
- Separate protocol documents from essays and archives.
- Add RFC format for protocol changes.
- Publish RFC 0001 for the Full Spectrum Protocol.
- Define minimum protocol objects:
  - identity declaration;
  - capability declaration;
  - permission request;
  - consent record;
  - risk alert;
  - ESS request/result;
  - guardian review;
  - audit trace.
- Keep object specifications under `specs/` and machine-readable contracts under `schemas/`.

## Phase 2: Schema and examples

Goal: make the protocol inspectable by developers.

- Add JSON schemas.
- Add identity and capability declaration schemas.
- Add audit trace schema.
- Add risk alert schema.
- Add external ethics profile schema.
- Add cross-enterprise audit record schema.
- Add FSHI request / response schemas.
- Add example audit traces.
- Add external node classification examples.
- Add FSHI customer-service quality inspection sample.
- Add minimal FSHI examples that convert desensitized dialogue into RiskAlert and AuditTrace.
- Add standards and ecosystem mapping for AIP, A2A, MCP, data-governance trends, and AI risk frameworks.
- Add an agent-oriented reading path that separates implementation artifacts from philosophical essays.
- Add minimal ESS simulation examples.
- Add cell protocol examples for organizations and AI agents.
- Add `specs/README.md` so implementers can find the engineering-facing objects quickly.

## Phase 3: Open-core implementation

Goal: make the protocol runnable.

- Create or link a minimal local-first engine repository.
- Provide desensitized multi-turn dialogue samples.
- Provide risk scoring and audit-output examples.
- Provide logistics and e-commerce adaptation examples.
- Provide a minimal FSHI API contract that maps product-facing inputs and outputs to RiskAlert and AuditTrace.
- Provide paired FSHI request/response schemas so inspection payloads can be checked before conversion into RiskAlert and AuditTrace.
- Provide a minimal validation script that checks the request -> response -> RiskAlert -> AuditTrace chain.
- Keep examples non-invasive: FSHI may recommend enterprise actions, but execution belongs to the enterprise unless explicit integration feedback exists.
- Explain the relationship between the local engine, Cell Protocol, and the future protocol network.
- Maintain a conformance and testing guide so contributors know what "validated" means at each stage.

## Current practical focus

At the moment, the most important public work is:

1. keep the protocol repository readable as a protocol repository;
2. keep schemas, RFCs, mappings, and examples internally consistent;
3. keep the engine repository versioned and reproducible;
4. keep enterprise-facing materials separated from protocol-core claims;
5. prepare for broader external review without overstating maturity.

## Phase 4: External review

Goal: invite critique before claiming maturity.

- Invite AI safety researchers.
- Invite software engineers.
- Invite ethics and governance reviewers.
- Invite industry users.
- Collect abuse cases and failure cases.
- Track unresolved disputes publicly.

## Phase 5: Governance and ecosystem

Goal: make the project able to evolve without being owned by a single interpretation.

- Establish maintainer roles.
- Establish guardian review flow.
- Establish protocol versioning.
- Establish compatibility vs certification policy.
- Establish compatibility and deprecation policy.
- Keep self-deconstruction and rollback mechanisms visible.

