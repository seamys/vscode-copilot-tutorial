# 01 - VS Code WebSearch MCP 配置教程

## 课程概述

本课程将教您如何在 VS Code 中配置 WebSearch MCP (Model Context Protocol) 扩展，实现 GitHub Copilot 的联网搜索功能。通过这个配置，您可以让 Copilot 能够访问最新的在线信息来辅助编程。

## 学习目标

完成本课程后，您将能够：
- 理解 MCP (Model Context Protocol) 的基本概念
- 安装和配置 WebSearch MCP 扩展
- 完成首次使用时的 GitHub 登录授权流程
- 获取和配置搜索引擎 API Key（Tavily 或 Bing）
- 使用 Copilot 进行联网搜索获取最新信息
- 了解联网搜索的最佳实践和使用场景
- 解决常见的登录和配置问题

## 前置条件

- VS Code 已安装
- GitHub Copilot 扩展已安装并激活
- 有效的 GitHub 账户（用于首次登录授权）
- 稳定的网络连接
- 搜索引擎 API Key（Tavily 或 Bing API Key）

## 配置步骤

### 步骤 1: 安装 WebSearch MCP 扩展

**方法 1: 通过链接直接安装 (推荐)**

点击以下链接直接安装扩展：
[WebSearch for Copilot 扩展](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-websearchforcopilot)

1. 点击上述链接，会打开 VS Code Marketplace 页面
2. 点击页面上的 "Install" 按钮
3. 浏览器会提示打开 VS Code，点击确认
4. VS Code 会自动开始安装扩展

**方法 2: 通过 VS Code 扩展面板安装**

1. 打开 VS Code
2. 按 `Ctrl+Shift+X` (Windows/Linux) 或 `Cmd+Shift+X` (Mac) 打开扩展面板
3. 搜索 `ms-vscode.vscode-websearchforcopilot` (扩展ID)
4. 找到由 **Microsoft (ms-vscode)** 发布的 "Web Search for Copilot" 扩展
   - 扩展ID: `ms-vscode.vscode-websearchforcopilot`
   - 描述: "Gives access to search engines from within Copilot"
5. 点击 "Install" 安装扩展

> **💡 搜索提示**: 直接搜索扩展ID `ms-vscode.vscode-websearchforcopilot` 是最可靠的方法。

### 步骤 2: 验证扩展安装

安装完成后，您可以通过以下方式验证：
- 在 VS Code 的扩展列表中看到 "Web Search for Copilot" 扩展已启用
- 扩展图标显示为绿色激活状态
- **扩展详细信息确认**:
  - 扩展名称: "Web Search for Copilot"
  - 发布者: Microsoft
  - 扩展ID: `ms-vscode.vscode-websearchforcopilot`
  - 描述: "Gives access to search engines from within Copilot"

> **✅ 验证提示**: 可以在扩展面板中搜索 `ms-vscode.vscode-websearchforcopilot` 来快速定位扩展。

### 步骤 3: 首次使用登录配置

当您第一次尝试使用 WebSearch 功能时，VS Code 会要求进行身份验证：

#### 3.1 GitHub 登录授权

1. **首次搜索触发**: 当您第一次向 Copilot 发起搜索请求时，VS Code 会弹出登录提示
2. **授权对话框**: 会出现以下提示窗口：
   ```
   The extension 'Web Search for Copilot' wants to sign in using GitHub.
   
   [Allow] [Cancel]
   ```
3. **点击 Allow**: 选择 "Allow" 按钮允许扩展使用 GitHub 登录
4. **浏览器跳转**: VS Code 会自动打开浏览器，跳转到 GitHub 授权页面
5. **GitHub 授权**: 在浏览器中按照提示完成 GitHub 账户授权
6. **返回 VS Code**: 授权完成后，浏览器会提示返回 VS Code

#### 3.2 搜索引擎配置

Web Search for Copilot 扩展支持两种搜索引擎：

**默认搜索引擎: Tavily**
- 扩展默认使用 Tavily 搜索引擎
- 需要获取 Tavily API Key 才能使用
- 提供更准确和丰富的搜索结果

**备选搜索引擎: Bing**
- 可以选择使用 Bing 搜索引擎作为替代
- 同样需要相应的 API Key

**配置 Tavily API Key（必需）:**

1. **访问 Tavily 网站**: 前往 [tavily.com](https://tavily.com) 注册账户
2. **获取 API Key**: 
   - 注册并登录 Tavily 账户
   - 在控制台中获取您的 API Key
3. **配置 API Key**: 
   - 打开 VS Code 设置 (`Ctrl+,` 或 `Cmd+,`)
   - 搜索 "tavily"
   - 在 "WebSearch: Tavily API Key" 设置中输入您的 API Key
   - **或者**：首次使用时，扩展会自动提示您输入 API Key

**切换搜索引擎:**
- 在 VS Code 设置中搜索 "websearch"
- 找到 `websearch.preferredEngine` 设置
- 可以选择 "Tavily"（默认）或 "Bing"

> **📝 重要提示**: 
> - **默认使用 Tavily 搜索引擎**，这是当前的默认配置
> - **必须配置 API Key** 才能使用搜索功能（无论选择哪种搜索引擎）
> - 首次使用时，扩展会引导您获取并配置 API Key
> - API Key 将安全存储在 VS Code 的内置密钥存储中

#### 3.3 验证配置

完成登录后，您可以通过以下方式验证配置是否成功：
- 在 Copilot Chat 中发起一个简单的搜索请求
- 观察是否能正常返回搜索结果
- 确认没有进一步的授权提示

### 步骤 4: 配置扩展设置 (可选)

1. 打开 VS Code 设置 (`Ctrl+,` 或 `Cmd+,`)
2. 搜索 "websearch"
3. 根据需要调整以下设置：
   - **搜索引擎选择**: 通过 `websearch.preferredEngine` 设置选择 Tavily（默认）或 Bing
   - **搜索引擎 API Key**: 配置相应搜索引擎的 API Key
   - **搜索结果数量**: 控制返回的搜索结果数量
   - **搜索超时时间**: 设置搜索请求的超时时间
   - **直接使用搜索结果**: 启用 `websearch.useSearchResultsDirectly` 可跳过后处理，直接使用原始搜索结果

## 使用方法

### 基础联网搜索

配置完成后，您可以通过以下几种方式使用联网搜索功能：

#### 方法 1: 自动搜索（推荐）
1. **打开 Copilot Chat**: 按 `Ctrl+Alt+I` 或点击侧边栏的 Copilot Chat 图标
2. **直接提问**: 如果启用了意图检测，Copilot 会自动识别需要联网搜索的问题

#### 方法 2: 使用 @websearch 参与者
1. **手动调用**: 在 Copilot Chat 中使用 `@websearch` 命令
2. **示例**: `@websearch 什么时候 VS Code 的 Workspace Trust 功能发布的？`

#### 方法 3: 使用 #websearch 工具
1. **结合其他参与者**: 可以与其他聊天参与者结合使用
2. **示例**: `@workspace /new #websearch 使用最流行的 Python 框架创建一个新的 Web 应用`

**示例提问:**
```
请搜索 React 19 的最新特性
```

```
搜索最新的 Python 3.12 新功能
```

```
查找最新的 VS Code 扩展开发最佳实践
```

### 编程场景中的联网搜索

在编程过程中，您可以请求 Copilot 搜索最新的技术信息：

**API 使用示例:**
```
搜索 OpenAI GPT-4 API 的最新参数配置方法
```

**框架更新:**
```
搜索 Next.js 14 的最新路由配置方式
```

**错误解决:**
```
搜索如何解决 TypeScript 5.0 的编译错误
```

## 实践练习

### 练习 1: 搜索最新技术信息

1. 打开 Copilot Chat
2. 询问一个最新的编程技术话题
3. 观察 Copilot 如何使用联网搜索获取最新信息
4. 比较有无联网搜索时 Copilot 回答的差异

### 练习 2: 解决实际编程问题

1. 创建一个新的 JavaScript 文件
2. 向 Copilot 询问最新的 JavaScript ES2024 特性
3. 请求相关的代码示例
4. 验证提供的信息是否为最新的

## 最佳实践

### 何时使用联网搜索

✅ **适合的场景:**
- 查询最新的 API 文档
- 了解框架的最新版本特性
- 寻找最新的最佳实践
- 解决最新版本的技术问题

❌ **不适合的场景:**
- 基础编程概念学习
- 已知稳定的语法规则
- 简单的代码补全任务

### 搜索查询优化

**有效的查询方式:**
- 明确指定版本号: "React 18 hooks 最佳实践"
- 包含时间限制: "2024年最新的 TypeScript 配置"
- 具体描述问题: "Next.js 14 app router 错误处理"

**避免的查询方式:**
- 过于宽泛: "JavaScript 教程"
- 过于简单: "什么是变量"
- 无时效性要求的基础问题

## 故障排除

### 常见问题

**问题 0: 在扩展市场搜索不到 WebSearch for Copilot 扩展**
- **解决方案**: 直接搜索扩展ID `ms-vscode.vscode-websearchforcopilot`
- **验证方法**: 确认找到的扩展发布者是 **Microsoft (ms-vscode)**

**问题 1: 首次使用时登录失败**
- **现象**: 首次搜索时出现 GitHub 登录提示，但登录失败或无响应
- **解决方案**: 
  - 确保网络连接正常，可以访问 GitHub
  - 点击 "Allow" 后耐心等待浏览器打开
  - 如果浏览器未自动打开，手动复制授权链接到浏览器
  - 清除 VS Code 的登录缓存：重启 VS Code 后重新尝试
  - 检查防火墙设置，确保允许 VS Code 访问网络

**问题 2: API Key 配置问题**
- **现象**: 首次使用时提示需要 API Key，或者搜索功能不工作
- **解决方案**:
  - 确认已在相应的搜索引擎服务商（Tavily 或 Bing）注册并获取了有效的 API Key
  - 在 VS Code 设置中正确配置 API Key
  - 验证 API Key 没有过期或达到使用限制
  - 确认选择的搜索引擎与配置的 API Key 匹配
  - 重启 VS Code 使配置生效

**问题 3: 联网搜索不工作**
- 检查是否已完成 GitHub 登录授权
- 确认扩展已正确安装并启用
- 验证网络连接是否正常
- 重启 VS Code

**问题 4: 搜索结果不相关**
- 尝试更具体的查询词
- 包含技术栈和版本信息
- 分步骤提问

**问题 5: 搜索速度慢**
- 检查网络延迟
- 调整搜索超时设置
- 简化查询内容
- 考虑配置 Tavily API Key 以提升性能

## 进阶技巧

### 组合使用技巧

1. **上下文结合**: 在现有代码基础上请求最新信息更新
2. **多步骤查询**: 先搜索概念，再请求具体实现
3. **比较分析**: 请求不同技术方案的最新对比

### 工作流集成

将联网搜索整合到日常开发流程中：
1. 项目启动时搜索最新的框架版本
2. 遇到错误时搜索最新的解决方案
3. 代码审查时验证最佳实践的时效性

## 总结

通过配置 WebSearch MCP 扩展，您已经成功为 GitHub Copilot 添加了联网搜索能力。这将显著提升 Copilot 在提供最新技术信息方面的能力，帮助您在编程过程中获得更准确、更及时的帮助。

记住始终保持查询的具体性和相关性，这样可以获得最佳的搜索结果和编程辅助效果。

## 下一步

- 探索其他 MCP 扩展的功能
- 学习如何优化 Copilot 的提示工程
- 了解 Copilot 的高级功能和最佳实践
