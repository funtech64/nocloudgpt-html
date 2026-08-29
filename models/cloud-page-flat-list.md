# Terminal Glass Cloud Page Creation Flat List

Date: 2026-06-18
Directory target: `/models/`

## Page rule

Each verified Ollama Cloud model gets its own Terminal Glass family folder directly under `/models/`:

```text
/models/<ollama-model-name>-cloud/index.html
```

These pages are for **Terminal Glass Cloud Instances**, not local NoCloudGPT instances. The sales copy should describe a cloud-accelerated Ollama/OpenWebUI workflow with low local hardware requirements.

## Verified cloud pages to create

1. `/models/gemma3-cloud/index.html` — `gemma3`
2. `/models/gemma4-cloud/index.html` — `gemma4`
3. `/models/qwen3.5-cloud/index.html` — `qwen3.5`
4. `/models/gpt-oss-cloud/index.html` — `gpt-oss`
5. `/models/qwen3-coder-cloud/index.html` — `qwen3-coder`
6. `/models/nemotron-3-super-cloud/index.html` — `nemotron-3-super`
7. `/models/glm-5-cloud/index.html` — `glm-5`
8. `/models/minimax-m2.5-cloud/index.html` — `minimax-m2.5`
9. `/models/glm-5.1-cloud/index.html` — `glm-5.1`
10. `/models/gemini-3-flash-preview-cloud/index.html` — `gemini-3-flash-preview`
11. `/models/minimax-m2.7-cloud/index.html` — `minimax-m2.7`
12. `/models/glm-4.7-cloud/index.html` — `glm-4.7`
13. `/models/deepseek-v3.2-cloud/index.html` — `deepseek-v3.2`
14. `/models/minimax-m2.1-cloud/index.html` — `minimax-m2.1`
15. `/models/qwen3-coder-next-cloud/index.html` — `qwen3-coder-next`
16. `/models/ministral-3-cloud/index.html` — `ministral-3`
17. `/models/devstral-small-2-cloud/index.html` — `devstral-small-2`
18. `/models/deepseek-v3.1-cloud/index.html` — `deepseek-v3.1`
19. `/models/nemotron-3-nano-cloud/index.html` — `nemotron-3-nano`
20. `/models/rnj-1-cloud/index.html` — `rnj-1`
21. `/models/kimi-k2.5-cloud/index.html` — `kimi-k2.5`
22. `/models/kimi-k2.6-cloud/index.html` — `kimi-k2.6`
23. `/models/devstral-2-cloud/index.html` — `devstral-2`
24. `/models/deepseek-v4-pro-cloud/index.html` — `deepseek-v4-pro`
25. `/models/deepseek-v4-flash-cloud/index.html` — `deepseek-v4-flash`
26. `/models/mistral-large-3-cloud/index.html` — `mistral-large-3`
27. `/models/minimax-m3-cloud/index.html` — `minimax-m3`
28. `/models/glm-5.2-cloud/index.html` — `glm-5.2`
29. `/models/kimi-k2.7-cloud/index.html` — `kimi-k2.7-code` (Terminal.Glass slug; same Ollama family as kimi-k2.7-code-cloud)
30. `/models/kimi-k2.7-code-cloud/index.html` — `kimi-k2.7-code`
31. `/models/nemotron-3-ultra-cloud/index.html` — `nemotron-3-ultra`

## Hold / do not build as cloud pages yet

These are useful model pages, but they are not confirmed cloud-tagged on the Ollama library page during this review:

1. `/models/qwen3.6-cloud/index.html` — hold. Current Ollama page shows `vision tools thinking 27b 35b`, but not `cloud`.
2. `/models/nemotron-cascade-2-cloud/index.html` — hold. Current Ollama page shows `tools thinking 30b`, but not `cloud`.

Build these as local/model-family pages only unless Ollama later adds the `cloud` tag.

## Notes

- `gemma3-cloud` was added to the flat build list because Ollama marks `gemma3` as cloud-supported and lists explicit cloud tags such as `gemma3:4b-cloud`, `gemma3:12b-cloud`, and `gemma3:27b-cloud`.
- `gemini-3-flash-preview-cloud` should include careful brand/legal wording because it is a preview/frontier cloud model and may have separate usage expectations.
- Every cloud page should use the Terminal Glass CTA: **Fast, efficient pre-built private AI workflow**.
