# macOS / Windows 环境配置

## 核心原则

GitHub 用来同步 Notebook、Python 文件和依赖清单，不同步虚拟环境本身。

- 每台电脑都在项目目录中单独创建 `.venv`；
- `.venv` 已写入 `.gitignore`，不会被提交；
- 两台电脑安装相同的 Python 大版本和 `requirements.txt`，可以得到功能一致的学习环境；
- macOS 和 Windows 的二进制包可能不同，因此不要复制另一台电脑的 `.venv` 文件夹。

推荐使用 **Python 3.11**。它可以覆盖本项目的 NumPy、Pandas、scikit-learn、Jupyter 和
PyTorch 学习内容，同时在 macOS 与 Windows 上都有较好的兼容性。

## Windows（PowerShell）

先安装 Python 3.11 和 VS Code 的 Python、Jupyter 扩展，然后在项目根目录运行：

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name python-learning --display-name "Python Learning (.venv)"
python test.py
```

如果 PowerShell 不允许执行激活脚本，可以改用“命令提示符”：

```bat
py -3.11 -m venv .venv
.venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## macOS（zsh）

在项目根目录运行：

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name python-learning --display-name "Python Learning (.venv)"
python test.py
```

## 安装 PyTorch

只使用 CPU，或暂时只学习基础 API 时，可以在激活 `.venv` 后运行：

```bash
python -m pip install -r requirements-torch.txt
```

Windows 电脑若有 NVIDIA 显卡并希望使用 CUDA，不要直接照搬 macOS 的安装结果，也不要固定
使用上面的普通安装命令。请在 PyTorch 官方安装页面选择 Windows、Pip、Python 和你的 CUDA
版本，然后在已激活的 `.venv` 中执行页面生成的命令。

安装后检查：

```bash
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
```

`torch.cuda.is_available()` 返回 `False` 不代表 PyTorch 安装失败：CPU 环境和 Apple Silicon
通常不会使用 CUDA。

## VS Code 选择解释器和 Notebook 内核

1. 用 VS Code 打开仓库根目录；
2. 打开 `.py` 文件时，执行 `Python: Select Interpreter`，选择项目中的 `.venv`；
3. 打开 `.ipynb` 时，点击右上角内核名称，选择 `Python Learning (.venv)`；
4. 如果刚安装的内核没有出现，重载 VS Code 窗口后再选；
5. 在 Notebook 中执行以下代码，确认当前使用的解释器：

```python
import sys

print(sys.executable)
```

路径应指向当前项目下的 `.venv`，而不是另一套全局 Python。

## 两台电脑之间的日常同步

开始学习前：

```bash
git pull
```

修改并确认 Notebook 已保存后：

```bash
git status
git add <你修改的文件>
git commit -m "update learning notes"
git push
```

如果 `requirements.txt` 有更新，拉取代码后重新运行：

```bash
python -m pip install -r requirements.txt
```

## 常见问题

### `ModuleNotFoundError`

通常是 VS Code 选错了 Python / Notebook 内核，或者包被安装到了另一套 Python。先检查：

```python
import sys

print(sys.executable)
```

再在同一个环境中使用 `python -m pip install ...`。这种写法比直接使用 `pip install ...`
更明确，因为它保证 `pip` 属于当前这个 Python。

### macOS 能运行，Windows 不能运行

先确认两边都是 Python 3.11，并在各自的 `.venv` 中安装了依赖。涉及文件路径时，优先使用
`pathlib.Path`，避免手写 `/` 或 `\`：

```python
from pathlib import Path

data_path = Path("data") / "example.csv"
```

### 是否要提交 Notebook 输出

学习笔记可以保留关键输出和图形，便于复习；大型、重复或包含本机路径的输出应在提交前清理。
