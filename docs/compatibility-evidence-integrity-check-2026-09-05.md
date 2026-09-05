# 跨仓库证据包完整性检查（2026-09-05）

**检查编号：** FS-COMPAT-EVIDENCE-001  
**结论：** `PASS_WITH_SCOPE_LIMITS`

## 检查对象

```text
https://github.com/full-spectrum-lab/full-spectrum-observer/raw/master/observer-ig5-evidence-20260905.zip
```

## 实际结果

```ini
DOWNLOAD = PASS
SHA256 = 00D26D2B488AACC29C114B7DD29400A8E160F416D31CB68068324D526755A5A4
EXPECTED_SHA256 = 00D26D2B488AACC29C114B7DD29400A8E160F416D31CB68068324D526755A5A4
HASH_MATCH = PASS
ARCHIVE_EXTRACTION = PASS
ARCHIVE_FILE_COUNT = 7
```

## 范围限制

该检查证明公开证据包可以下载、解压且哈希一致；不证明 Protocol、Engine、Observer 三仓库版本兼容关系已经通过正式组合验收。

Observer 证据包内部锁定的 Engine worker 版本与当前兼容矩阵候选版本不能直接等同，必须另行执行 Protocol/Engine/Observer 的版本映射和固定 fixture 测试。

```ini
EVIDENCE_INTEGRITY = PASS
VERSION_COMPATIBILITY = NOT_CONFIRMED
PRODUCTION_VALIDATION = NO
```
