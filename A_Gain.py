for i in range(int(input())):
    n = int(input())
    temp = list(map(int, input().split()))

    left = [0]*n
    right = [0]*n
    l_max = float('-inf')
    r_max = float('-inf')
    ans = []

    for i in range(n):
        if i == 0:
            left[i] = float('-inf')
            right[n - 1 - i] = float('-inf')
            continue

        left[i] = max(l_max, temp[i - 1])
        right[n - 1 - i] = max(r_max, temp[n - i])
        l_max = left[i]
        r_max = right[n - 1 - i]
    
    for i in range(n):
        ans.append(temp[i] - max(left[i], right[i]))
    print(' '.join(map(str, ans)))
