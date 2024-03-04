from collections import Counter
for i in range(int(input())):
    n, m, k = map(int, input().split())
    temp1 = Counter(input().split())
    temp2 = Counter(input().split())

    difference1 = 0
    difference2 = 0
    common = 0

    for tem in temp1:
        if int(tem) <= k and tem in temp2:
            common += 1
        elif int(tem) <= k:
            difference1 += 1
    for tem in temp2:
        if int(tem) <= k and tem not in temp1:
            difference2 += 1
    
    if difference2 + difference1 + common < k:
        print('NO')
    elif difference1 > k//2 or difference2 > k//2:
        print('NO')
    else:
        print('YES')

