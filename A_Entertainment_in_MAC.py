for i in range(int(input())):
    k = int(input())
    s = input()

    l = 0
    r = len(s) - 1

    while r > l:
        if s[r] == s[l]:
            r -= 1
            l += 1
        else:
            break
    if s[l] <= s[r]:
        print(s)
    else:
        print(s[::-1] + s)

