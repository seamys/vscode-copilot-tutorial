# GitHub Copilot 数据转换与网页抓取教程

## 📚 学习目标

本教程将教你如何使用 GitHub Copilot 来：
- 实现网页数据抓取
- 使用正则表达式清理数据
- 进行数据格式转换
- 创建结构化 JSON 输出
- 实现错误处理和进度显示

## 🎯 任务描述

从维基百科 [国家人口列表页面](https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population) 抓取国家人口数据，转换为指定JSON格式并保存文件。

## 期望输出格式

```json
{
  "countries": [
    {
      "rank": 1,
      "country": "China",
      "population": 1412000000,
      "percentage_of_world": 17.9,
      "date": "2023", 
      "source": "Official estimate"
    }
  ],
  "metadata": {
    "last_updated": "2025-09-03",
    "total_countries": 50,
    "data_source": "Wikipedia - List of countries and dependencies by population",
    "url": "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
  }
}
```

## 要求

- 使用正则表达式清理数据（移除逗号、括号等）
- 实现完整的错误处理
- 显示友好的进度提示
- 保存为格式化JSON文件