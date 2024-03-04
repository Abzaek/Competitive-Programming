for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = [abs(x) for x in arr]

    l = 0
    r = n - 1

    print(sum(arr))
