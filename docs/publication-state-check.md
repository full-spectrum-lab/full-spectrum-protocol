# 发布状态检查器

`tools/check_publication_state.py` 是只读检查器，用于防止状态文件把本地提交误报为远端发布。

示例：

```text
python tools/check_publication_state.py \
  --repo <repository> \
  --status <repository>/status/full-spectrum-status.yaml \
  --remote-ref origin/main
```

返回含义：

- `COMMIT_PRESENT`：声明的提交在本地可解析；
- `REMOTE_REACHABLE`：提交可从指定远端引用到达；
- `REMOTE_UNKNOWN`：无法确认远端引用；
- `REMOTE_NOT_REACHABLE`：提交存在，但不能证明已发布到该远端引用；
- `INVALID`：声明的提交不存在。

该工具不会修改状态文件，也不会把 `UNKNOWN`、`NOT_CONFIRMED` 或 `LOCAL_ONLY` 自动升级为正向状态。
