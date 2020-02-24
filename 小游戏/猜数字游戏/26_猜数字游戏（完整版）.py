# 猜数字游戏


print('侏罗纪时代……')
print('天空下着大雨……')
print('你被恐龙骗到了一间废弃的实验室中，这时候你发现了一道暗门')
print('门上字迹斑驳，依稀可辨：猜数字游戏，请输入0~100内的数字，' +
      '如果猜对门会自动打开，注意你只有6次机会。')

import random

n = random.randint(0, 100)
count = 6

while True:
    # 接受用户的输入
    ni = int(input('请输入要猜的数字:'))

    count -= 1
    if count == 0:
        print('你身后传来了恐龙沉重的呼吸声')
        print('游戏结束')
        break

    if ni > n:
        print('猜大了，请继续')
        print('你还剩%s次机会，恐龙离你更近了' % count)
        # continue
    elif ni < n:
        print('猜小了，请继续')
        print('你还剩%s次机会，恐龙离你更近了' % count)
        # continue
    else:
        print('猜对了,一阵白光，你逃离了侏罗纪世界')
        break
