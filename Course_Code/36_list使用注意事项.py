# list的所有用法总结
# 增、删、改、查
# 增：append、insert
# 删：pop
# 改：赋值形式覆盖，完成修改
# 查：list[下标] for x in list

#几点list使用时的注意事项
# 技能列表
skill_list = ['一墨横空', '墨度迷津', '墨之纵横', '墨下乾坤']
# 下标可以是正，从0开始
# 也可以是负，从-1开始，-1表示最后一个元素，-2表示倒数第二个元素，以此类推
# print(skill_list[-1])
# print(skill_list[-2])



# print('------------')

# print(skill_list[4])
# print(skill_list[-5])

for i in range(len(skill_list)):
    print(skill_list[i])
