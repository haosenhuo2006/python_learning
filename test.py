"""快速检查学习环境中的核心依赖。"""

from importlib import import_module


PACKAGES = ["numpy", "pandas", "matplotlib", "sklearn", "torch"]


def main() -> None:
    for package in PACKAGES:
        try:
            module = import_module(package)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK]      {package:<12} {version}")
        except ImportError:
            print(f"[MISSING] {package:<12} 请在当前 Python 环境中安装")


if __name__ == "__main__":
    main()
