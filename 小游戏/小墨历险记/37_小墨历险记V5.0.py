# 小墨历险记V5.0

import random

print('欢迎来到墨家村，如今是妖兽的地盘')
print('历经九死一生，你来到了boss狂风的老巢')

# 定义boss和玩家的血量
hp_boss = 100
hp_player = 100

print('boss狂风的血量为' + str(hp_boss) + '，请准备开始战斗！')

# 定义技能：为了能够统一处理技能和普通攻击，把普通攻击也作为一个技能
skill_list = ['一墨横空', '墨度迷津', '墨之纵横', '墨下乾坤', '普通攻击']
# 技能对应的伤害值
skill_attack = [20, 30, 40, 50, 10]

while True:
    for i in range(1, 6):
        # i : 1 2 3 4 5
        print('请输入数字%s释放第%s个技能：%s,基础伤害：%s' % (i, i, skill_list[i - 1], skill_attack[i-1]))
    # 使用技能攻击
    print('请输入数字1、2、3、4、5，攻击boss狂风')
    ni = int(input())
    if ni == 1 or ni == 2 or ni == 3 or ni == 4 or ni == 5:
        # 玩家打出的随机伤害值：定义好的技能对应的伤害 + 随机1~5
        attack_player = skill_attack[ni - 1] + random.randint(1, 5)
        # boss扣血
        hp_boss -= attack_player
        if hp_boss < 0:
            hp_boss = 0
        print('你使用%s攻击了boss狂风，打出了%s的伤害，boss狂风的剩余血量为%s' 
              % (skill_list[ni - 1], attack_player, hp_boss))

        if hp_boss > 0:
            # boss的反击伤害
            attack_boss = random.randint(30, 50)
            # 玩家扣血
            hp_player -= attack_boss
            if hp_player < 0:
                hp_boss = 0
            print('愤怒的狂风进行了反击，打出了%s的伤害，你当前剩余血量为%s' 
                  % (attack_boss, hp_player))
            # 判断玩家是否已死亡
            if hp_player == 0:
                  print('很遗憾，你未能完成冒险……')
                  break
        else:
            print('恭喜你!打败了boss狂风!!!')
            break
    else:
        print('请输入数字1、2、3、4、5进行战斗!!!')
    

