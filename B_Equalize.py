for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)

    for j in range(1, n + 1):
        arr[j - 1] += j
    arr.sort()

    res = 0
    l = 0

    for j in range(n):
        while arr[l] != arr[j]:
            l += 1
        res = max(res, j - l + 1)
        
    print(res)


