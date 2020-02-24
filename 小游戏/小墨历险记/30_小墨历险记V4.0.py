# 小墨历险记V4.0
# boss反击

import random

print('欢迎来到墨家村，如今是妖兽的地盘')
print('经历九死一生，你来到了boss狂风的老巢')

hp_boss = 100
hp_player = 100
print('狂风的血量为' + str(hp_boss) + '，准备开始战斗！')

while True:
    print('请输入数字1，攻击boss狂风')
    ni = int(input())
    if ni == 1:
        # 小墨的攻击力
        attack_player = random.randint(10, 20)
        # boss血量
        hp_boss -= attack_player
        print('你打出了%s的伤害，boss狂风的剩余血量为%s' % (attack_player, hp_boss))
        # 判断boss是否已经死亡
        if hp_boss > 0:
            # boss的反击伤害
            attack_boss = random.randint(10, 20)
            print('愤怒的boss狂风对你进行了反击，伤害值为%s' %(attack_boss))
            hp_player -= attack_boss
            print('你当前剩余血量为%s' % (hp_player))
            if hp_player <= 0:
                  print('很遗憾，游戏失败')
                  break
        else:
            print('恭喜你，打败了boss狂风')
    else:
        print('请输入数字1进行战斗!!!')
    
