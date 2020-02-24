# for循环
# 计算1~100内所有数字的相加之和
# range(n):用于生成0~n-1的整数序列
sum = 0
for x in range(101):
    sum += x
print('相加之和为：%s' % sum)
