# for循环
# 30x + 8y = 1980

for x in range(1001):
    for y in range(1001):
        if 30 * x + 8 * y == 1980:
            print('30x + 8y = 1980, x = %s, y = %s' % (x, y))
