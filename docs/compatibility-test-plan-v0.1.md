# Full Spectrum 最小兼容性测试计划 v0.1

**状态：** PROPOSED  
**目的：** 为 Protocol、Engine、Observer 的最小组合兼容性提供可追踪证据。

## 测试范围

1. 使用固定 Protocol schema 和版本字段；
2. 运行 Engine 固定 fixture；
3. 将 Engine 输出交给 Observer evidence/replay 入口；
4. 检查 provenance、版本、身份边界和限制字段是否保留；
5. 记录成功、失败、未执行和环境限制。

## 最小矩阵

| Protocol | Engine | Observer | 当前状态 |
|---|---|---|---|
| draft | `v1.4.0` | `v0.3.0-beta.2` | `REPORTED_COMPATIBILITY` |
| draft | `v1.5.0` | `v0.4.0-beta` | `NOT_CONFIRMED` |

## 通过条件

- schema 校验通过；
- Engine 输出可被 Observer 读取；
- provenance 和版本信息无丢失；
- replay 结果可重复；
- 失败路径有明确错误码或记录；
- 证据包包含测试环境、提交、时间和 SHA-256。

## 边界

- 固定 fixture 通过不等于生产兼容；
- 离线复现不等于真实网络验证；
- 版本号存在不等于兼容关系成立；
- 报告性结论必须先标 `REPORTED_*`，经证据确认后才可升级。

## 结果记录模板

```yaml
test_id: FS-COMPAT-001
as_of: "<timestamp>"
protocol_version: "<version>"
engine_version: "<version>"
observer_version: "<version>"
status: NOT_EXECUTED
scope: OFFLINE
commits:
  protocol: "<commit>"
  engine: "<commit>"
  observer: "<commit>"
evidence_bundle: null
evidence_bundle_sha256: null
limitations:
  - REAL_NETWORK_NOT_EXECUTED
```
