# FDE-TRIAL-001 Acceptance Matrix 0.1.0-rc

Created at: 2026-09-10 19:13 (Beijing time, UTC+8)

Last updated at: 2026-09-10 19:13 (Beijing time, UTC+8)

Status: `FIXTURE_FREEZE_CANDIDATE`

This matrix validates a synthetic, pinned, local-offline governance exercise. It does not validate real refunds, real networks, general compatibility, or production readiness.

| Gate | Claim | Required evidence | Current state |
|---|---|---|---|
| FDE-01 | All six inputs conform to the Protocol Schema | Validator log | READY_NOT_EXECUTED_IN_CI |
| FDE-02 | Canonical JSON digests match the manifest | RFC 8785 validator log | READY_NOT_EXECUTED_IN_CI |
| FDE-03 | Observer projection preserves protected fields | Field-level comparison | NOT_EXECUTED |
| FDE-04 | Engine returns REVIEW_REQUIRED / FIXTURE_EXPECTATION_ONLY / FAIL | Pinned runtime output | NOT_EXECUTED |
| FDE-05 | Audit persists before human decision | KG persistence log | NOT_EXECUTED |
| FDE-06 | Unauthorized, expired, or absent approval fails closed | Negative test log | NOT_EXECUTED |
| FDE-07 | FakeActionSink remains zero before approval | Action counter evidence | NOT_EXECUTED |
| FDE-08 | Approved simulation executes at most once | ActionSink idempotency evidence | NOT_EXECUTED |
| FDE-09 | SQLite close/reopen Replay preserves digests | Replay log | NOT_EXECUTED |
| FDE-10 | Tampering with input, output, binding, or audit is rejected | Negative test log | NOT_EXECUTED |
| FDE-11 | Three identical runs produce identical canonical digests | Three run manifests | NOT_EXECUTED |
| FDE-12 | A non-implementing instance reproduces the package | Independent report | NOT_EXECUTED |

Fixture freeze requires FDE-01 and FDE-02 plus responsibility-domain review. Implementation authorization is a separate decision. Runtime, network, and production status cannot be derived from fixture validation.
