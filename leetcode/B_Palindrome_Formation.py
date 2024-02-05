for i  in range(int(input())):
    n = int(input())
    s = input()
    s_reversed = s[::-1]

    _count = 0
    pntr = 0
    flag = True

    while pntr < (n+1)//2:
        if s[pntr] != s_reversed[pntr]:
            if _count == 1:
                flag = False
                print('No')
                break
            else:
                _count += 1
                while pntr < len(s) and s[pntr] != s_reversed[pntr]:
                    pntr += 1
        pntr += 1

    if flag:
        print('Yes')
                