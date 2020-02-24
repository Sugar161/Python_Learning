# 小墨历险记v6.0

def background():
    print('游戏开始……')
    print('欢迎来到墨家村，如今是妖兽的地盘')

# 挑选角色
hero_list = [
        {'index':1, 'name':'墨小小', 'hp':1000, 'mp':800, 'ap':45, 'dp':20, 
         'skills':['一墨横空', '墨度迷津', '墨之纵横', '墨下乾坤'], 'skills_hp':[20, 45, 75, 100], 
         'is_warrior': True, 'is_mage': False, 'is_hunter': False},

        {'index':2, 'name':'墨小妹', 'hp':1200, 'mp':700, 'ap':35, 'dp':21, 
         'skills':['貂蝉拜月', '西施捧心', '昭君出塞', '贵妃醉酒'], 'skills_hp':[18, 23, 47, 82], 
         'is_warrior': True, 'is_mage': True, 'is_hunter': False},

        {'index':3, 'name':'墨大元', 'hp':1100, 'mp':600, 'ap':38, 'dp':17, 
         'skills':['千里横行', '寒刀断水', '狂龙破日', '天地无情'], 'skills_hp':[26, 51, 80, 102], 
         'is_warrior': True, 'is_mage': False, 'is_hunter': True},

        {'index':4, 'name':'墨当归', 'hp':900, 'mp':1100, 'ap':44, 'dp':17, 
         'skills':['流水行云', '披星戴月', '翻云覆雨', '排山倒海'], 'skills_hp':[23, 45, 80, 97], 
         'is_warrior': False, 'is_mage': True, 'is_hunter': False},

        {'index':5, 'name':'墨鱼儿', 'hp':1000, 'mp':1000, 'ap':42, 'dp':23, 
         'skills':['小楫轻舟', '扁舟一叶', '大江似练', '沧波万顷'], 'skills_hp':[19, 39, 68, 92], 
         'is_warrior': False, 'is_mage': False, 'is_hunter': True},
    ]

# 挑选角色
def select_hero(hero_list):
    print('请输入职业或姓名筛选角色，输入角色编号选择角色……')
    # 所有角色展示
    for x in hero_list:
        print('编号:%s, 姓名：%s' % (x.get('index'), x.get('name')))
    # 不定次数的循环
    while True:
        ni = input()
        if ni == '1' or ni == '2' or ni == '3' or ni == '4' or ni == '5':
            hero = hero_list[int(ni) - 1]
            print('你选择了:%s' % (hero.get('name')))
            return hero
        elif ni == '战士':
            # 把所有的战士的信息展示
            continue
        elif ni == '法师':
            # 把所有的法师的信息展示
            continue
        elif ni == '猎人':
            # 把所有的猎人的信息展示
            continue
        else:
            # 把对应模糊查询出的角色的信息展示出来
            continue

# 主方法定义
def main():
    background()
    select_hero(hero_list)

main()
    
