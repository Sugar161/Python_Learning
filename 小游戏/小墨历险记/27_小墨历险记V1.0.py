# 小墨历险记V1.0

print('欢迎来到墨家村，如今是妖兽的地盘')
print('经历九死一生，你来到了boss狂风的老巢')

hp_boss = 10
print('狂风的血量为' + str(hp_boss) + '，准备开始战斗！')

for x in range(10):
    print('请输入数字1，攻击boss狂风')
    ni = int(input())
    if ni == 1:
        hp_boss -= 1
        print('boss狂风的剩余血量为%s' % (hp_boss))
        if hp_boss == 0:
            print('恭喜你，打败了boss狂风')
    
    
