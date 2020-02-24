# 小墨历险记V3.0
# 随机攻击 3~5

import random

print('欢迎来到墨家村，如今是妖兽的地盘')
print('经历九死一生，你来到了boss狂风的老巢')

hp_boss = 10
print('狂风的血量为' + str(hp_boss) + '，准备开始战斗！')

while True:
    print('请输入数字1，攻击boss狂风')
    ni = int(input())
    if ni == 1:
        # 小墨的攻击力
        attack_player = random.randint(3, 5)
        # boss血量
        hp_boss -= attack_player
        print('你打出了%s的伤害，boss狂风的剩余血量为%s' % (attack_player, hp_boss))
        if hp_boss <= 0:
            print('恭喜你，打败了boss狂风')
    else:
        print('请输入数字1进行战斗!!!')
    
    
