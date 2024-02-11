for i in range(int(input())):
    n = int(input())
    p = 1
    temp = list(map(int, input().split()))
    temp.sort()

    for i, num in enumerate(temp):

        if num > p:
            print('NO')
            break
        else:
            if i != 0:
                p += num
            if i == len(temp) - 1:
                print('YES')

