# 打印文件内容

with open(r'd:\python_learning\numpy_studying.ipynb', 'r', encoding='utf-8') as f:
    content = f.read()

# 打印前2000个字符
print('文件前2000个字符:')
print('=' * 50)
print(content[:2000])