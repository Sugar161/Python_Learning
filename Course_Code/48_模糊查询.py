# 墨家村英雄榜2.0
heroes_list = [
    {'name':'墨小小', 'hp':1000, 'mp':800, 'ap':45, 'dp':20, 
     'skills':['一墨横空', '墨度迷津', '墨之纵横', '墨下乾坤'],
     'is_warrior': True, 'is_mage': False, 'is_hunter': False},

    {'name':'墨小妹', 'hp':1200, 'mp':700, 'ap':35, 'dp':21, 
     'skills':['貂蝉拜月', '西施捧心', '昭君出塞', '贵妃醉酒'],
     'is_warrior': True, 'is_mage': True, 'is_hunter': False},

    {'name':'墨大元', 'hp':1100, 'mp':600, 'ap':38, 'dp':17, 
     'skills':['千里横行', '寒刀断水', '狂龙破日', '天地无情'],
     'is_warrior': True, 'is_mage': False, 'is_hunter': True},

    {'name':'墨当归', 'hp':900, 'mp':1100, 'ap':44, 'dp':17, 
     'skills':['流水行云', '披星戴月', '翻云覆雨', '排山倒海'],
     'is_warrior': False, 'is_mage': True, 'is_hunter': False},

    {'name':'墨鱼儿', 'hp':1000, 'mp':1000, 'ap':42, 'dp':23, 
     'skills':['小楫轻舟', '扁舟一叶', '大江似练', '沧波万顷'],
     'is_warrior': False, 'is_mage': False, 'is_hunter': True},
]

# 查找所有战士的姓名
for x in heroes_list:
    if x ['is_warrior']:
        print(x['name'])

print('-' * 20)

# 获取所有战士的的技能列表
for x in heroes_list:
    if x ['is_warrior']:
        print(x['name'] + '的技能有：')
        for skill in x['skills']:
            print(skill)

print('-' * 20)


# 根据用户输入的姓名查找对应的血量
# 精确查询
input_name = input('请输入要查找的姓名：')
for x in heroes_list:
    if x['name'] == input_name:
        print('%s的血量为:%s' % (x['name'], x['hp']))

print('-' * 20)

# 模糊查询
name = '小墨'
# 判断一个字符串中是否包含另一个字符串
# 字符串 = 一堆字符串的集合
if '大' in name:
    print('匹配')
else:
    print('不匹配')

print('-' * 20)

# 模糊查询的第二种方法：
if name.find('大') != -1:
    print('匹配')
else:
    print('不匹配')























        
