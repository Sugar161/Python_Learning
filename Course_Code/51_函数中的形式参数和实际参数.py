# 输出3遍Hello
# 输出5遍World
# 输出4遍Hello
# 输出5遍World
# 输出3遍Hello
# 输出3遍World
# 函数小括号中的数据，称为函数的参数
# 具体来说，函数定义时的数据，称为形式参数
def a(n):
    for i in range(n):
        print('Hello')
        
def b(n):
    for i in range(n):
            print('World')
# 函数使用时指定的数据，称为实际参数
# 实际参数，用于给形式参数赋值
a(3)

b(5)

a(4)

b(5)

a(3)

b(3)
