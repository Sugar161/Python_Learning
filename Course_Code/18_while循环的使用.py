# 请计算1-100内所有的数字相加之和

n = 100
sum = 0
while n > 0:
    # sum = sum + n
    sum += n
    # n = n - 1
    n -= 1
print('计算结果为:%s' % sum)
