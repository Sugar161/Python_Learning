# for循环
# ABCD*E=DCBA

for A in range(10):
    for B in range(10):
        if A == B:
            continue
        
        for C in range(10):
            if A == C or B == C:
                continue
            
            for D in range(10):
                if A == D or B == D or C == D:
                    continue
                
                for E in range(10):
                    if A == E or B == E or C == E or D == E:
                        continue

                    x = 1000*A + 100*B + 10*C +D
                    y = 1000*D + 100*C + 10*B +A
                    
                    if x * E == y:
                        print(A, B, C, D, E)
                        
