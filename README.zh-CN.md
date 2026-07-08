# 全频谱协议

> 面向 AI 时代主体协作的开放治理语义协议：人、AI Agent、组织、系统与跨组织网络。

全频谱协议是一座桥，不是强制中心。它不替代法律、监管、企业合规、A2A、MCP、国家智能体互联标准或人工最终判断。它定义的是连通层之上的治理层：行动依据、边界声明、风险显影、审计追踪、责任路径与复核接口。

English readers can start from [README.md](./README.md).

---

## 当前状态

本仓库处于早期开源协议草案与工程探索阶段。

当前提供：

- 协议总纲与 RFC；
- 机器可校验 schema；
- 合成样例；
- 标准映射与业务场景映射；
- FSHI 客服质检参考方向；
- 指向最小可运行治理引擎的工程入口；`r`n- 面向生态说明与对外图示的共享公共素材。

本仓库不宣称：

- 已经成为全球正式标准；
- 已经获得任何监管认可；
- 可以替代法律、安全监管、企业合规或人工复核；
- 已经包含成熟商业产品完整代码；
- 证明任何个人、组织或系统可以代表“整体”。

---

## 为什么需要它

AI 系统正在变得更快、更自主，也更深地嵌入真实组织。现有互联协议可以帮助智能体发现彼此、交换消息、调用工具、同步任务状态。

全频谱关注的是下一层问题：

- 这次行动为什么被允许？
- 谁在行动？
- 它声明了什么能力与边界？
- 检测到了什么风险？
- 如果造成后果，责任路径如何记录？
- 哪些内容需要留给后续复核？
- 什么时候应该降级、暂停、熔断或请求人工复核？
- 系统什么时候应该知道“我不知道，所以不该行动”？

一句话：

> 连通协议让 Agent 能一起行动；全频谱协议关注连接之后如何保持可审计、可问责、可知边界。

---

## 全频谱不是什么

全频谱不是：

- 新宗教或精神权威；
- 世界政府；
- 法律、人权、安全监管或企业合规的替代品；
- 已完成的 AI 安全万能方案；
- 商业 SaaS 产品；
- 要求所有外部系统必须加入全频谱网络的强制体系；
- “有了协议就一定安全”的证明。

它是一套协议草案、schema 集合和开放工程路径，目标是让 AI 相关行动更可见、可复核、可追责。

---

## 与现有标准和生态的关系

全频谱不替代 A2A、MCP、LangGraph、国家智能体互联标准、数据治理体系或 AI 风险框架。

这些体系主要回答连通层和基础设施问题：

- 智能体如何标识自己；
- 能力如何描述；
- 如何发现彼此；
- 如何交换消息和任务；
- 如何调用工具；
- 数据如何治理与流通。

全频谱关注这些交互周围的治理层：

- 行动依据；
- 风险声明；
- 审计追踪；
- 责任路径；
- 边界自知；
- 复核与升级；
- 跨组织审计记录。

相关入口：

- [协议映射中心](./docs/mapping/README.md)
- [标准与生态映射](./docs/mapping/standards-mapping.md)
- [跨企业审计记录映射](./docs/mapping/cross-enterprise-audit-record-mapping.md)
- [FSHI API 合同映射](./docs/mapping/fshi-api-contract-mapping.md)

---

## 30 秒入口

- 如果你只是想调用一个外部 AI 工具，请看 [External Node Guide](./EXTERNAL_NODE_GUIDE.md)。
- 如果你已有 AI 系统，只想兼容接入而不申请完整认证，请看 [RFC 0005](./rfcs/0005-node-classification-and-external-ethics-profile.md)。
- 如果你需要跨组织共享审计记录，请看 [RFC 0006](./rfcs/0006-cross-enterprise-audit-record.md)。
- 如果你需要身份与能力声明，请看 [RFC 0002](./rfcs/0002-identity-and-capability-declaration.md)。
- 如果你需要风险与审计对象，请看 [RFC 0003](./rfcs/0003-audit-trace-schema.md) 和 [RFC 0004](./rfcs/0004-risk-alert-schema.md)。
- 如果你想看业务工程样例，请看 [FSHI API Contract Mapping](./docs/mapping/fshi-api-contract-mapping.md)。
- 如果你想参与协议改进，请看 [RFC 0001](./rfcs/0001-full-spectrum-protocol.md)。

---

## 最小治理链路

一个最小的全频谱兼容流程可以描述为：

```text
原始 AI 行动
  -> Governance Event
  -> 业务适配器
  -> 标准上下文
  -> 层级画像
  -> 引擎 / 策略 / 安全检查
  -> RiskAlert / AuditTrace / Runestone
  -> 人工或组织复核
```

当前项目不要求一个系统先加入全球协议网络才能尝试这条链路。企业或开发者可以先在内部部署本地优先引擎，用合成数据或脱敏数据进行验证。

---

## 协议地图

| 层级 | 回答的问题 | 典型产物 |
| --- | --- | --- |
| 身份层 | 谁在行动？ | 身份声明、数字身份声明 |
| 能力层 | 它能做什么？ | 能力声明、边界声明 |
| 权限层 | 当前允许做什么？ | 授权、同意、撤销 |
| 责任层 | 谁承担责任？ | AuditTrace、责任路径 |
| 推演层 | 不同条件下可能发生什么？ | ESS 情境推演 |
| 风险层 | 何时减速、降级、停止或升级？ | RiskAlert、熔断、恢复报告 |
| 复核层 | 无单一主体可独断时谁来复核？ | 守庙人复核、组织复核、人工复核 |
| 演化层 | 协议如何变化而不成为新的牢笼？ | RFC、版本、反例 |

---

## 工程参考：FSHI

FSHI（Full Spectrum Health Index，全频谱健康指数）在本仓库中作为 AI 客服质检的工程参考。

在本仓库中，FSHI 是：

- 一个协议用例；
- 一个合成与脱敏样例方向；
- 一个 API 合同映射练习；
- 一个非侵入式多轮对话风险检测示例；
- 一座从治理语义到业务工程的桥。

它在这里不是完整商业产品实现。

建议边界：

- `full-spectrum-protocol`：协议、schema、RFC、样例、审计格式。
- `full-spectrum-engine`：最小可运行、本地优先治理引擎。
- 私有或公司仓库：客户适配、生产部署、商业资产、真实企业数据。

---

## 本地优先采用路径

全频谱不应强制采用。

更实际的路径是：

1. **企业内部引擎层**：在单个组织内部，用合成或脱敏案例运行本地引擎。
2. **细胞协议层**：为一个主体或系统声明身份、能力、边界、权限与责任。
3. **协议网络层**：当多个主体需要交互时，再引入节点注册、跨节点审计、ESS 复核、守庙人复核与贡献记录。

当前仓库重点在第一步和第二步。

---

## 机器校验

当前仓库校验：

- Markdown、JSON、YAML、HTML、CSS、脚本文件中的常见乱码模式；
- 部分协议对象的 schema 与样例一致性；
- FSHI 对话检测合同链：

```text
request.sample.json
  -> response.sample.json
  -> risk-alert.sample.json
  -> audit-trace.sample.json
  -> cross-enterprise-audit-record.example.json
```

校验会在推送和 Pull Request 到 `main` 时通过 GitHub Actions 运行。

---

## 推荐阅读顺序

1. [START_HERE.md](./START_HERE.md)
2. [Full Spectrum Protocol Outline v0.1](./docs/protocols/full-spectrum-protocol-outline-v0.1.md)
3. [Glossary](./docs/glossary.md)
4. [Specifications](./specs/README.md)
5. [External Node Guide](./EXTERNAL_NODE_GUIDE.md)
6. [RFC 0001: Full Spectrum Protocol](./rfcs/0001-full-spectrum-protocol.md)
7. [RFC 0002: Identity and Capability Declaration](./rfcs/0002-identity-and-capability-declaration.md)
8. [RFC 0003: Audit Trace Schema](./rfcs/0003-audit-trace-schema.md)
9. [RFC 0004: RiskAlert Schema](./rfcs/0004-risk-alert-schema.md)
10. [RFC 0005: Node Classification and External Ethics Profile](./rfcs/0005-node-classification-and-external-ethics-profile.md)
11. [RFC 0006: Cross-Enterprise Audit Record Profile](./rfcs/0006-cross-enterprise-audit-record.md)
12. [协议映射中心](./docs/mapping/README.md)
13. [FSHI 客服质检用例](./docs/use-cases/FSHI_Customer_Service_Quality_Inspection.md)
14. [Conformance and Testing Guide](./docs/testing/conformance-and-testing-guide.md)
15. [Validations](./validations/)
16. [ROADMAP.md](./ROADMAP.md)

---

## 贡献

欢迎提交批评、反例、翻译、schema、样例和改进建议。

请阅读：

- [CONTRIBUTING.md](./CONTRIBUTING.md)
- [GOVERNANCE.md](./GOVERNANCE.md)
- [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)

---

## 安全提示

不要在本仓库存放 token、密码、Cookie、私钥、未脱敏个人信息、未授权企业数据或真实客户数据。


