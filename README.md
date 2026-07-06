# Python Learning Notes

这套笔记按“基础语法 → 数组计算 → 数据分析 → 数学基础 → 机器学习 → 深度学习”组织。原笔记中的有效内容均以保留为原则，只合并重复部分，并增加直观解释、数学推导、图形和详细代码注释。

## 推荐学习顺序

| 顺序 | Notebook | 重点 |
|---:|---|---|
| 1 | `tryit.ipynb` | Python 语法、容器、函数、异常、类 |
| 2 | `numpy_studying.ipynb` | shape、axis、广播、向量化 |
| 3 | `pandas_studying.ipynb` | 清洗、筛选、分组、合并、管道 |
| 4 | `math_foundations_for_ml.ipynb` | 导数、偏导数、梯度、Jacobian、Hessian、反向传播 |
| 5 | `machine_learning.ipynb` | 损失、梯度下降、评估、泄漏、调参 |
| 6 | `LiMu_Deep_learning.ipynb` | 原笔记主线：Tensor、数据预处理、线性代数、自动求导 |
| 可选 | `deep_learning_extensions.ipynb` | DataLoader、训练循环、nn.Module、MLP |

## 使用方式

1. 在 VS Code 中打开 `python_learning.code-workspace`；
2. 选择安装了对应依赖的 Python / Jupyter 内核；
3. 从 C++ 转向 Python 时，先完成 `tryit.ipynb` 的“语言地图”部分；
4. 每节先阅读说明并预测输出，再运行代码；
5. 遇到错误先检查变量类型、数组形状和当前执行顺序；
6. 完成每本末尾练习后，再看参考答案。

## 环境

推荐统一使用 Python 3.11，并在每台电脑的项目目录中单独创建 `.venv`。基础依赖安装：

```bash
python -m pip install -r requirements.txt
```

深度学习笔记还需要 PyTorch。CPU / 普通学习环境可以安装：

```bash
python -m pip install -r requirements-torch.txt
```

Windows NVIDIA CUDA 环境需要按显卡和 CUDA 版本选择 PyTorch 安装命令。完整的 macOS、
Windows、VS Code 内核和两台电脑同步说明见 [`ENVIRONMENT.md`](ENVIRONMENT.md)。
不要提交或复制 `.venv`；GitHub 只同步代码、笔记和依赖清单。

## 文件说明

- 六个 `.ipynb` 是主学习材料，另有一本可选深度学习扩展；
- `numpy_tutorial.py` 是 NumPy 重点的脚本版复习；
- `test.py` 用于快速检查学习环境；
- `print_file.py` 用于列出 Notebook 的章节和单元数量。
- `requirements.txt` 是基础依赖清单；
- `requirements-torch.txt` 在基础依赖上增加 PyTorch；
- `ENVIRONMENT.md` 说明 macOS / Windows 环境配置和同步方式。

## 学习方法

- 每次只学一个概念，并修改示例观察结果；
- 利用已有 C++ 基础建立对应关系，但不要把 Python 名称绑定当成 C++ 值拷贝；
- 为数组标注形状，例如 `X: (m, n)`、`w: (n,)`；
- 不只记 API，要说清输入、输出和为什么这样做；
- 学数学公式时先拆成中间变量，再写每一步的局部导数；
- 看到梯度时检查它是否与对应参数 shape 相同；
- 用数值梯度验证手推结果，避免只背最终公式；
- 机器学习实验要固定随机种子并记录数据划分；
- 学完一章后，用空白 Notebook 独立重写一个小例子。
