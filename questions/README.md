# 题目格式说明

## 概览

每个模块有两类文件：

| 文件 | 用途 |
|------|------|
| `yanyu.json` | App 直接读取，不要手动编辑 |
| `yanyu.csv` | **题目源文件**，用 Excel/记事本编辑 |

## 加题步骤

1. 打开对应模块的 CSV 文件（Excel 最方便）
2. 在最后一行照着格式填：

```
id,type,knowledge,question,options,answer,explanation
yy021,single,选词填空,把句子补充完整,用|||分隔选项,1,对选项含义的解析
```

3. 保存 CSV
4. 运行 `scripts/build_questions.py`，它会自动把 CSV 转成 JSON 并推送到 GitHub
5. 刷新 App 页面，新题就出现了

## 字段说明

| 字段 | 必填 | 说明 |
|------|------|------|
| id | 是 | 唯一标识，如 `yy021`，不要和已有重复 |
| type | 是 | 题型：`single`（单选题）或 `multi`（多选题） |
| knowledge | 是 | 知识点，如 `选词填空`、`行程问题` |
| question | 是 | 题干，可以包含换行（\n） |
| options | 是 | 选项，用 `\|\|\|` 分隔，如 `A项\|\|\|B项\|\|\|C项\|\|\|D项` |
| answer | 是 | 正确答案索引，从 0 开始：0=A, 1=B, 2=C, 3=D |
| explanation | 是 | 解析，解释为什么选这个 |

## 注意事项

- **不要手动编辑 JSON** — 每次运行 `build_questions.py` 会覆盖 JSON，修改会丢失
- **不要在选项里用 `|||`** — 这是分隔符
- **answer 从 0 开始**，不是从 1 开始
- 多选题用 `multi`，answer 用逗号分隔如 `0,2` 表示选 AC

## 批量加题建议

把题目整理成表格：

| id | type | knowledge | question | options | answer | explanation |
|----|------|-----------|----------|---------|--------|-------------|
| yy021 | single | 选词填空 | ... | A\|\|\|B\|\|\|C\|\|\|D | 2 | ... |

然后复制到 CSV 文件末尾。
