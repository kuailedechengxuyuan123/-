# 缺陷报告模板

## 标题
一句话描述缺陷（简洁、明确）

## 优先级 / 严重度
- 优先级: P1/P2/P3
- 严重度: Blocker/Critical/Major/Minor/Trivial

## 环境
- 操作系统: Windows/macOS/Linux
- Python 版本: 3.xx
- 运行方式: VSCode / CLI

## 前置条件
（复现步骤之前需要满足的条件，例如已登录、数据库有数据）

## 复现步骤
1. 打开项目，执行 `pytest tests/test_linear_search.py` 或在 VSCode 中运行
2. 在 `src/math_funcs.py` 第 10 行设置断点
3. 观察循环行为

## 期望结果
描述在正确行为下应当观察到的结果

## 实际结果
记录实际观察到的结果（包括错误信息、堆栈、截图链接）

## 附件
- 日志文件
- 报告文件（例如 report.html）
- 屏幕截图
