# 输出3遍Hello
# 输出5遍World
# 输出4遍Hello
# 输出5遍Hello
# 计算某个数的n次方 默认参数

def print_str(n, s = 'Hello'):
    for i in range(n):
        print(s)

print_str(3)
print_str(5, 'World')
print_str(4)
print_str(5)
