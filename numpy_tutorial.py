"""NumPy 重点复习脚本。

主笔记见 numpy_studying.ipynb。本脚本适合在终端快速复习并验证输出。
"""

import numpy as np


def show(title: str, value) -> None:
    """打印带标题的结果，便于对照每一步。"""
    print(f"\n{'=' * 12} {title} {'=' * 12}")
    print(value)


def main() -> None:
    rng = np.random.default_rng(42)

    # 约定：行是样本，列是特征。
    X = np.array([
        [170.0, 65.0],
        [180.0, 80.0],
        [160.0, 55.0],
    ])
    show("基本属性", {
        "shape": X.shape,
        "ndim": X.ndim,
        "size": X.size,
        "dtype": X.dtype,
    })

    # axis=0 压缩行，得到每一列（每个特征）的统计量。
    mean = X.mean(axis=0, keepdims=True)
    std = X.std(axis=0, keepdims=True)
    X_scaled = (X - mean) / std  # (3,2) 与 (1,2) 广播
    show("按列标准化", X_scaled)

    # 布尔数组可直接筛选满足条件的元素或行。
    tall_people = X[X[:, 0] >= 170]
    show("身高至少 170 的行", tall_people)

    # @ 是矩阵乘法：每个样本的两个特征乘各自权重再相加。
    weights = np.array([0.3, -0.2])
    predictions = X_scaled @ weights
    show("线性预测 X @ weights", predictions)

    # 新随机数接口不会污染全局随机状态，固定 seed 后可复现。
    sample = rng.normal(loc=0, scale=1, size=(2, 3))
    show("可复现随机样本", sample)


if __name__ == "__main__":
    main()
