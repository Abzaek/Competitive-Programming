for i in range(int(input())):
    n = int(input())
    temp = list(map(int, input().split()))
    r = n - 1
    l = 0

    while l < n - 1 and temp[l] == temp[l + 1]:
        l += 1

    while r > 0 and temp[r - 1] == temp[r]:
        r -= 1

    if l >= n - 1:
        print(0)
    elif temp[r] == temp[l]:
        print(r - l - 1)
    else:
        if n - 1 - r > l - 0:
            print(r)
        else:
            print(n - 1 - l)