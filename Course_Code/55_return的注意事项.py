# return的注意事项

def a():
    for i in range(4):
        if i == 2:
            # return会直接结束方法
            return
        print(i)

a()

