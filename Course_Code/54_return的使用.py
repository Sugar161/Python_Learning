# Python函数中return的使用

# 定义一个方法，用于得到传入参数的绝对值
#return : 返回

def my_abs(n):
    if n >= 0:
        return n
    else:
        return -n

print(my_abs(2) + 100)
print(my_abs(-2) + 100)
