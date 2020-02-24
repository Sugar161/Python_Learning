for i in range(1, 6):
    for j in range(1, 6 - i):
        print(' ')
        j += 1
    for k in range(2 * i - 1):
        print('*')
        k += 1
    print('\n')
    i += 1
