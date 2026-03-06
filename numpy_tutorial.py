import numpy as np

def print_section(title):
    """打印章节标题，增强可读性"""
    print("\n" + "="*50)
    print(f"  {title}")
    print("="*50)

def print_step(step_name, data=None):
    """打印步骤提示和数据"""
    print(f"\n>>> [步骤] {step_name}:")
    if data is not None:
        print(data)

# ==========================================
# 模块 1：NumPy 数组基础属性
# ==========================================
print_section("1. NumPy 数组的基础属性")

# 创建一个 2x3 的矩阵
# np.array() 将 Python 列表转换为 NumPy 数组
array = np.array([[1, 2, 3],
                  [1, 2, 3]])

print_step("创建原始矩阵", array)

# 核心概念解释：
# ndim: 维度数（数组的秩），即有几层嵌套
# shape: 形状，返回一个元组，表示 (行数, 列数)
# size: 元素总个数，即 行 * 列
print(f"  - 维度 (ndim): {array.ndim}")
print(f"  - 形状 (shape): {array.shape}")
print(f"  - 元素个数 (size): {array.size}")

# dtype: 数组中元素的数据类型
# 可以手动指定，如 dtype=np.int32, np.float64 等
a_int = np.array([2, 23, 4], dtype=int)
a_float = np.array([2, 23, 4], dtype=float)

print_step("数据类型演示")
print(f"  - 整数类型数组: {a_int}, 类型: {a_int.dtype}")
print(f"  - 浮点数类型数组: {a_float}, 类型: {a_float.dtype}")


# ==========================================
# 模块 2：特殊数组的创建与形状变换
# ==========================================
print_section("2. 特殊数组的创建与形状变换")

# np.zeros: 创建全 0 矩阵
# np.ones: 创建全 1 矩阵
# np.empty: 创建“空”矩阵，其值是内存中原有的数据（接近 0）
print_step("全 0 矩阵 (3x4)", np.zeros((3, 4)))
print_step("全 1 矩阵 (5x4)", np.ones((5, 4), dtype=int))
print_step("未初始化矩阵 (3x4)", np.empty((3, 4)))

# np.arange: 生成等差序列 (起始, 终点, 步长) -> 左闭右开
# reshape: 重新调整数组的维度
print_step("等差序列 (10到20, 步长2)", np.arange(10, 20, 2))
print_step("序列重构为 3x4 矩阵", np.arange(12).reshape((3, 4)))

# np.linspace: 生成线段序列 (起始, 终点, 元素个数)
print_step("线段序列 (1到10, 均匀取5个点)", np.linspace(1, 10, 5))
print_step("线段序列重构为 2x3 矩阵", np.linspace(1, 10, 6).reshape((2, 3)))


# ==========================================
# 模块 3：基础数学运算
# ==========================================
print_section("3. 基础数学运算")

a = np.array([10, 20, 30, 40])
b = np.arange(4) # [0, 1, 2, 3]

print(f"  - 数组 A: {a}")
print(f"  - 数组 B: {b}")

# 对应位置相加减
print_step("A - B", a - b)
print_step("A + B", a + b)

# 乘方运算
print_step("B 的平方 (B**2)", b**2)

# 三角函数 (作用于每个元素)
print_step("10 * sin(A)", 10 * np.sin(a))

# 逻辑判断 (返回布尔数组)
print_step("判断 B 中哪些值小于 3", b < 3)


# ==========================================
# 模块 4：矩阵乘法（核心区别）
# ==========================================
print_section("4. 矩阵乘法：逐位乘 vs. 矩阵积")

A = np.array([[1, 1],
              [0, 1]])
B = np.arange(4).reshape((2, 2)) # [[0, 1], [2, 3]]

print(f"  - 矩阵 A:\n{A}")
print(f"  - 矩阵 B:\n{B}")

# 逐位乘法 (*): 相同位置的数字直接相乘
print_step("逐位乘法 (A * B)", A * B)

# 矩阵乘法 (dot): 线性代数中的矩阵积运算
# 结果的第(i,j)个元素是 A 的第 i 行与 B 的第 j 列的内积
res_dot1 = np.dot(A, B)
res_dot2 = A.dot(B) # 等效写法

print_step("矩阵积 (np.dot(A, B))", res_dot1)


# ==========================================
# 模块 5：统计与排序
# ==========================================
print_section("5. 统计、排序与范围约束")

# 生成随机矩阵
data = np.random.random((2, 4))
print_step("原始随机数据", data)

# 聚合运算：sum, min, max
# axis=0 表示对“列”操作（垂直方向）
# axis=1 表示对“行”操作（水平方向）
print(f"  - 总和: {np.sum(data):.4f}")
print(f"  - 每列最小值 (axis=0): {np.min(data, axis=0)}")
print(f"  - 每行最大值 (axis=1): {np.max(data, axis=1)}")

# 更多统计函数
A = np.arange(14, 2, -1).reshape((3, 4))
print_step("统计用矩阵 A", A)

print(f"  - 最小值的索引 (argmin): {np.argmin(A)}")
print(f"  - 最大值的索引 (argmax): {np.argmax(A)}")
print(f"  - 平均值: {np.mean(A)}")
print(f"  - 中位数: {np.median(A)}")

# 累计求和 (cumsum): 展示数值演变过程
print_step("累计求和 (cumsum)", np.cumsum(A))

# 差分运算 (diff): 相邻元素的差值
print_step("相邻元素差分 (diff)", np.diff(A))

# clip: 边界值截断（非常有用的数据预处理工具）
# 将 A 中小于 5 的数改为 5，大于 9 的数改为 9
print_step("数值截断 (clip, 范围5到9)", np.clip(A, 5, 9))


# ==========================================
# 模块 6：索引、切片与迭代
# ==========================================
print_section("6. 索引、切片与迭代")

A = np.arange(3, 15).reshape((3, 4))
print_step("操作矩阵 A", A)

# 索引访问
print(f"  - A[2]: 获取第 3 行: {A[2]}")
print(f"  - A[1, 1]: 获取第 2 行第 2 列: {A[1, 1]}")
print(f"  - A[2, :]: 获取第 3 行所有数 (切片): {A[2, :]}")
print(f"  - A[1, 1:3]: 获取第 2 行中索引 1 到 2 的数: {A[1, 1:3]}")

# 迭代
print_step("按行迭代打印:")
for row in A:
    print(f"    行数据: {row}")

# 转置迭代 (间接按列迭代)
print_step("按列迭代打印 (通过转置实现):")
for col in A.T:
    print(f"    列数据: {col}")

# 扁平化迭代 (迭代每一个元素)
print_step("扁平化迭代 (打印前 5 个元素):")
count = 0
for item in A.flat:
    print(item, end=" ")
    count += 1
    if count >= 5: break
print("...")


# ==========================================
# 模块 7：合并与分割
# ==========================================
print_section("7. 矩阵合并与维度增加")

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])

print(f"  - A: {A}, B: {B}")

# vstack: 垂直合并 (Vertical stack)
print_step("垂直合并 (vstack)", np.vstack((A, B)))

# hstack: 水平合并 (Horizontal stack)
print_step("水平合并 (hstack)", np.hstack((A, B)))

# np.newaxis: 增加维度（常用于将一维向量转为矩阵）
print_step("增加行维度 A[np.newaxis, :]", A[np.newaxis, :])
print(f"    形状变化: {A.shape} -> {A[np.newaxis, :].shape}")

print_step("增加列维度 A[:, np.newaxis]", A[:, np.newaxis])
print(f"    形状变化: {A.shape} -> {A[:, np.newaxis].shape}")

# concatenate: 指定轴合并（通用合并方式）
A_col = A[:, np.newaxis]
B_col = B[:, np.newaxis]
res_cat = np.concatenate((A_col, B_col, B_col), axis=1) # 水平合并
print_step("使用 concatenate 在 axis=1 合并", res_cat)

print("\n" + "="*50)
print("  NumPy 教程运行结束")
print("="*50)
