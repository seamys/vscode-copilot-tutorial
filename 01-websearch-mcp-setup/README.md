# 01 - VS Code WebSearch MCP 配置教程

## 概述

配置 WebSearch MCP 扩展，让 GitHub Copilot 能够联网搜索最新信息。

## 前置条件

- VS Code + GitHub Copilot 扩展
- GitHub 账户
- 网络连接

## 安装步骤

### 1. 安装扩展

**方法 1: 直接链接 (推荐)**
点击链接安装：[WebSearch for Copilot](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-websearchforcopilot)

**方法 2: 扩展面板**
1. 按 `Ctrl+Shift+X` 打开扩展面板
2. 搜索：`ms-vscode.vscode-websearchforcopilot`
3. 点击 "Install"

### 2. 首次使用配置

1. **GitHub 授权**：首次搜索时会提示登录，点击 "Allow" 完成授权
2. **API Key 配置**：
   - 访问 [tavily.com](https://tavily.com) 获取免费 API Key
   - 在 VS Code 设置中搜索 "tavily" 并配置 API Key

## 使用方法

配置完成后，在 Copilot Chat 中直接提问即可：

```
搜索 React 19 的最新特性
```

```
查找 Python 3.12 新功能
```

**使用提示**：
- 自动识别：Copilot 会自动判断是否需要联网搜索
- 手动指定：使用 `@websearch` 强制联网搜索
- 结合使用：`@workspace /new #websearch 使用最新的框架创建项目`

## 常见问题

**Q: 找不到扩展？**
A: 直接搜索扩展ID `ms-vscode.vscode-websearchforcopilot`

**Q: 首次登录失败？**
A: 检查网络连接，重启 VS Code 后重试

**Q: 搜索不工作？**
A: 确认已配置 Tavily API Key，检查 VS Code 设置中的 "tavily" 配置

**Q: 搜索结果不相关？**
A: 使用更具体的查询词，包含版本号和技术栈信息
