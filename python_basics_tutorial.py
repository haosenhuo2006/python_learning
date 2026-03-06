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
# 模块 1：Python 数据类型概览
# ==========================================
print_section("1. Python 核心数据类型")

# 整数 (int): 唯一一种整数类型，不限大小
a_int = 1
print_step("整数示例", a_int)

# 布尔型 (bool): True 或 False
a_bool = True
print_step("布尔型示例", a_bool)

# 浮点数 (float): 带有小数点的数，支持科学计数法
a_float = 1.23
a_sci = 3E-2
print_step("浮点数示例", f"{a_float}, {a_sci}")

# 复数 (complex): 由实部和虚部组成
a_complex = 1 + 2j
print_step("复数示例", a_complex)


# ==========================================
# 模块 2：字符串操作详解
# ==========================================
print_section("2. 字符串的操作与处理")

# 字符串定义: 单引号, 双引号, 三引号
s1 = 'hello'
s2 = "world"
s3 = """这是一个
多行字符串"""
print_step("字符串定义", f"'{s1}', '{s2}', \n{s3}")

# 转义与原始字符串 (Raw string)
print_step("转义与原始字符串对比")
print(f"  - 使用 \\n: hello\nworld")
print(f"  - 使用 r 前缀: {r'hello\nworld'}") # r 前缀让反斜杠失效

# 字符串索引与切片 (Slicing)
# 格式: str[start:end:step] -> 左闭右开
s = '123456789'
print_step(f"字符串切片示例 (原始: {s})")
print(f"  - s[0:-1]: 从第一个到倒数第二个: {s[0:-1]}")
print(f"  - s[2:5]: 索引 2 到 4: {s[2:5]}")
print(f"  - s[1:8:2]: 步长为 2: {s[1:8:2]}")
print(f"  - s * 2: 重复两次: {s * 2}")
print(f"  - s + '你好': 连接字符串: {s + '你好'}")


# ==========================================
# 模块 3：输出控制与换行
# ==========================================
print_section("3. 控制 print 输出与换行")

x = 'Python'
y = 'Learning'

# print 默认会换行，通过 end 参数可以修改末尾字符
print_step("默认换行输出:")
print(x)
print(y)

print_step("不换行输出 (使用 end=' '):")
print(x, end=" ")
print(y)


# ==========================================
# 模块 4：基础流程控制
# ==========================================
print_section("4. 基础流程控制：If-Else 与多行语句")

# 基础判断逻辑
print_step("If-Else 逻辑演示")
flag = True
if flag:
    print("  - 条件满足：执行 True 分支")
else:
    print("  - 条件不满足：执行 False 分支")

# 多行语句：使用反斜杠 \ 进行换行
print_step("使用反斜杠 \\ 编写多行语句")
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
        item_two + \
        item_three
print(f"  - 1 + 2 + 3 = {total}")

print("\n" + "="*50)
print("  Python 基础教程运行结束")
print("="*50)
