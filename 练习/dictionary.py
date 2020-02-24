import random

name_list = ['Alise', 'Bob', 'Cindy']
num = len(name_list)

stu_info = []
stu_info_2 = []

# 方法1：stu_info包含num个小列表，对应每个人的姓名和年龄
for i in range(num):
    age = random.randint(0, 51)
    stu_i = [name_list[i], age]
    stu_info.append(stu_i)

print("方法1:")
for i in stu_info:
    print(i)


# 方法2：stu_info包含姓名列表和年龄列表
age_list = []
for i in range(num):
    age = random.randint(0, 51)
    age_list.append(age)

stu_info_2.append(name_list)
stu_info_2.append(age_list)

print("\n方法2:")
for i in range(num):
    print([stu_info_2[0][i], stu_info_2[1][i]])


# len(x):返回列表长度
# type(x):返回x的类型
