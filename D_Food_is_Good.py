def testines():
    
    n = int(input())

    temp = list(map(int, input().split()))
    p_sum = [0]*n
    p_sum[0] = temp[0]
    r = 0
    min_look = 0
    lookup = {'min_look': -1}

    for i in range(1, n):
        p_sum[i] = temp[i] + p_sum[i - 1]
    
    while r < n:
        if min(min_look, p_sum[r]) == p_sum[r]:
            lookup['min_look'] = r
        min_look = min(min_look, p_sum[r])


        while r < n - 1 and p_sum[r] <= p_sum[r + 1]:
            r += 1
        if lookup['min_look'] == -1:
            if p_sum[r] - min_look >= p_sum[-1]:
                if r >= n - 1:
                    print('YES')
                    return
                
                print('NO')
                return
        else:
            if p_sum[r] - min_look >= p_sum[-1]:
                print('NO')
                return
        r += 1
    print('YES')

for i in range(int(input())):    
    testines()

