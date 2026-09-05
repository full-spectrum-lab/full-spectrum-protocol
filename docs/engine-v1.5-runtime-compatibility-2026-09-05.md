# Engine v1.5 Runtime Compatibility Check（2026-09-05）

**测试对象：** 本地 `full-spectrum-engine-github-v15` 运行时  
**测试命令：** `python -m pytest -q tests/test_compat.py`

```ini
TESTS = 5
PASSED = 5
FAILED = 0
ENGINE_V1.5_COMPAT_API = PASS
ENGINE_V1.5_RUNTIME_SOURCE = LOCAL_V15_CHECKOUT
OBSERVER_LOCKED_IG5_RUNTIME = V1.0.0
PRODUCTION_COMPATIBILITY = NO
```

该结果确认 Engine v1.5 自身的兼容 API 测试通过，但它不是 Observer IG5 worker lock 的替换运行，也不构成三仓库端到端兼容验收。Observer 当前已发布证据包仍准确标注其锁定 Engine v1.0.0；本报告为 Engine v1.5 独立运行时证据。
