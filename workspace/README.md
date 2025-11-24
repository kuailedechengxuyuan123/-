# 测试实验项目 (样例)

本项目演示在 VSCode 中完成从实现、单元测试、调试到生成测试报告的完整学生实验流程。

主要内容：
- 被测代码：`src/math_funcs.py`（包含 `calculate` 与 `linear_search`）
- 单元测试：`tests/test_calculate.py`, `tests/test_linear_search.py`
- 简单的 Web 登录示例测试：`tests/test_web_login.py`（基于 `requests`）
- VSCode 调试配置：`.vscode/launch.json`
- 依赖：`requirements.txt`

环境 & 依赖

1. Python 3.10+
2. 在 PowerShell 中安装依赖：

```powershell
pip install -r requirements.txt
```

运行测试与生成报告

```powershell
# 生成 html 报告与 coverage
pytest --maxfail=1 -q --html=report.html --self-contained-html --cov=src
```

在 VSCode 中调试

1. 打开 `tests/test_calculate.py`（或其他测试文件），在感兴趣的行设置断点。
2. 在 Run and Debug 面板选择 `Debug test_calculate.py` 配置并启动调试。
3. 观察变量面板（例如 `iterations`、`i`、`found`）以完成基本路径测试与循环内部/外部测试。

如何用作课堂实验

- 引导学生先阅读 `src/math_funcs.py` 并预测分支行为。
- 让学生在 `tests` 中添加边界与更多循环案例（例如空数组、大量元素）。
- 演示如何在调试器中观察每次循环迭代（使用 `trace=True` 调用）并记录执行次数。
