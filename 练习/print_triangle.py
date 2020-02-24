# 方法一：
for i in range(1, 11):
    for j in range(1, i):
        print('*', end = '')
    print('*')

print('-' * 20)

# 方法二：
for i in range(1, 11):
    a = ''
    for j in range(1, i+1):
        a += "*"
    print(a)
