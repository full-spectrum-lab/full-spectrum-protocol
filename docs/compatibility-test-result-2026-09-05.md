# 最小兼容性验证结果（2026-09-05）

**测试编号：** FS-COMPAT-001  
**结论：** `PARTIALLY_EXECUTED`  
**证据等级：** 组合验证尚未完成，不升级为 `PASS`。

## 已执行并通过

| 检查 | 结果 | 说明 |
|---|---|---|
| Observer 状态 YAML 对统一 Schema 校验 | PASS | `full-spectrum-status.yaml` 校验通过 |
| Observer manifest 自洽性 | PASS | 300/300 文件匹配，无缺失、无多余 |
| Observer 独立复验脚本 | PASS | 26/26 场景通过 |
| Observer IG5 reference pipeline / Engine Facade worker smoke | PASS | CASE005 golden、输出摘要、Observation 和 Audit 检查通过；`formal_gate` 仍为 `NOT_PASSED` |
| Protocol 状态 Schema CI | PASS | GitHub Actions 已通过 |

## 尚未执行

- Protocol schema → Engine fixture → Observer replay 的正式端到端兼容链路；当前仅完成 Observer 内部 IG5 reference pipeline，未证明 C#/.NET 正式运行时；
- `v1.5.0` 与 `v0.4.0-beta` 的正式兼容声明；
- 真实网络请求、真实凭据和生产部署验证。

## .NET 运行时尝试

Observer `scripts/test.ps1 -Gate IG1` 已在补齐仓库要求的 .NET SDK `10.0.301` 后执行成功：IG0 baseline `51/51 PASS`，Release 构建 `0 warnings / 0 errors`。此外，Unit 与 Contract 测试分别全部通过（Unit 5 项、Contract 5 项）。

尚未执行 IG3/IG4/IG5/IG6 的完整门禁，因为这些门禁还需要仓库指定的私有 Python 运行时和固定 win-x64 SQLite 原生目录。

## 当前状态

```yaml
test_id: FS-COMPAT-001
as_of: "2026-09-05T00:00:00+08:00"
protocol_version: unreleased-or-draft
engine_version: v1.5.0
observer_version: v0.4.0-beta
status: PARTIALLY_EXECUTED
scope: OFFLINE
evidence_bundle: null
evidence_bundle_sha256: null
limitations:
  - END_TO_END_COMPOSITE_REPLAY_NOT_EXECUTED
  - REAL_NETWORK_NOT_EXECUTED
  - REAL_CREDENTIALS_NOT_READ
  - PRODUCTION_DEPLOYMENT_NOT_CONFIRMED
  - IG3_IG4_IG5_REQUIRE_PRIVATE_PYTHON_AND_SQLITE_RUNTIME
```

**解释：** 当前结果证明状态文件、Observer 自洽性和 Observer 独立复验链路有效，但不能证明 Protocol、Engine、Observer 三者已经完成正式兼容性验收。
