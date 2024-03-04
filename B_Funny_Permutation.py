t = int(input())
for i in range(t):
    n = int(input())

    if n == 3:
        print(-1)
    else:
        temp = [str(j) for j in range(n//2 + 1, n + 1)]
        for k in range(1, n//2 + 1):
            temp.append(str(k))

        print(' '.join(temp))
