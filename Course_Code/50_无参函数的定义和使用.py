# 输出3遍Hello
# 输出5遍World
# 输出4遍Hello
# 输出5遍World
# 输出3遍Hello
# 输出3遍World

def a():
    for i in range(3):
        print('Hello')
        
def b():
    for i in range(5):
            print('World')

a()

b()

for i in range(4):
    print('Hello')

b()

a()

for i in range(3):
    print('World')
