# 行测刷题助手 (study_assistant)

> 碎片化刷题 + 知识点库 + 智能分析，GitHub 驱动，长期迭代

## 核心功能

### 🎯 刷题系统
- 五大模块：常识 / 言语 / 数量 / 判断 / 资料
- 单题计时，随时退出，进度自动保存
- 错题自动入库，支持按知识点复习
- GitHub Gist 存储做题记录

### 📖 知识点库
- 按模块分类，结构化存储老师发的知识点
- 截图/文本发给我，我帮你整理入库
- 刷题时自动关联薄弱知识点

### 📊 数据分析
- 各模块正确率统计
- 薄弱知识点识别与推荐
- 进步曲线追踪

## 技术方案

- **前端**：单页 HTML + CSS + JavaScript (PWA)
- **数据存储**：GitHub Gist (做题记录) + 本仓库 (题库/知识点)
- **部署**：GitHub Pages (免费托管)
- **维护**：Mavis (我来长期维护和迭代)

## 目录结构

```
study_assistant/
├── src/                 # 源代码
│   ├── index.html       # 主页面
│   ├── styles.css       # 样式
│   └── app.js           # 逻辑
├── questions/           # 题库 (按模块分类)
│   ├── changshi.json    # 常识判断
│   ├── yanyu.json      # 言语理解
│   ├── shuliang.json   # 数量关系
│   ├── panduan.json    # 判断推理
│   └── ziliao.json     # 资料分析
├── knowledge/           # 知识点库
│   ├── changshi.md
│   ├── yanyu.md
│   ├── shuliang.md
│   ├── panduan.md
│   └── ziliao.md
├── data/                # 用户数据模板
│   └── gist-schema.json
├── docs/                # 文档
│   ├── CHANGELOG.md
│   └── ROADMAP.md
└── README.md
```

## 版本规划

### v1.0 MVP (当前)
- [x] 五大模块刷题
- [x] 单题计时
- [x] 随时退出，进度保存
- [x] 基础判分
- [ ] GitHub Gist 数据同步

### v1.x 迭代
- [ ] 错题本
- [ ] 薄弱点分析
- [ ] 知识点库
- [ ] PWA 安装

### v2.0 长期
- [ ] 智能出题 (Mavis 根据薄弱点生成变体题)
- [ ] 全真模考套卷
- [ ] 成就系统
- [ ] 复习提醒

## 在线使用

**访问地址**：https://feiguang50-hub.github.io/study_assistant/

手机/电脑直接打开链接即可使用！支持添加到手机桌面（类似App）。

## 使用方式

1. 打开上面的链接
2. 选择模块，开始刷题
3. 随时退出，进度自动保存（localStorage）
4. 把知识点发给 Mavis，帮你整理入库

## 数据同步（未来）

目前数据保存在浏览器本地（localStorage）。未来会接入 GitHub Gist 实现多设备同步。

---

> 由 Mavis 驱动 | Powered by MiniMax Code
