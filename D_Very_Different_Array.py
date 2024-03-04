# 5 5
# 3 6 7 9 10 
# 2 3 5 9 9
for i in range(int(input())):
    n, m = map(int, input().split())
    arr1= list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    arr1.sort()
    arr2.sort(reverse=True)
    l = 0
    r = 0
    _sum = 0

    while l < n and arr2[r] > arr1[l]:
        _sum  += arr2[r] - arr1[l]
        r += 1
        l += 1
    if l == n:
        print(_sum)
    else:
        l = n - 1
        r = m - 1
        while l > -1 and arr2[r] <= arr1[l]:
            _sum += arr1[l] - arr2[r]
            l -= 1
            r -= 1
    print(_sum)



