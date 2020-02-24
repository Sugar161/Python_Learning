for a in range(1, 5):
    for b in range(0, 9):
        for c in range(0, 9):
            
            abc = a * 100 + b * 10 + c

            # 甲：这个三位数能被2整除3次
            T1 = abc % 8 == 0
            # 乙：这个三位数能被3整除2次
            T2 = abc % 9 == 0
            # 丙：这个三位数能被7整除
            T3 = abc % 7 == 0
            # 丁：这个三位数的各个数字之和是15
            T4 = a + b + c == 15

            if T1 is True and T2 is True and T3 is True:
                print('丁说谎，abc = %s' % (abc))
            elif T1 is True and T2 is True and T4 is True:
                print('丙说谎，abc = %s' % (abc))
            elif T1 is True and T3 is True and T4 is True:
                print('乙说谎，abc = %s' % (abc))
            elif T2 is True and T3 is True and T4 is True:
                print('甲说谎，abc = %s' % (abc))
