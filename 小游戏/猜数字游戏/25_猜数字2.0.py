# 给定要猜的数字
import random

n = random.randint(0, 100)

# 不定次数的循环  死循环 + break/continue
while True:
    # 接受用户的输入
    ni = int(input('请输入要猜的数字:'))
    if ni > n:
        print('猜大了，请继续')
        # continue
    elif ni < n:
        print('猜小了，请继续')
        # continue
    else:
        print('猜对了')
        break
