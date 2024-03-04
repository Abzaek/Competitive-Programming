for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    md = sum(arr)% 3
    if md == 0:
        print(0)
    else:
        for i in range(n):
            if arr[i] % 3 == md:
                print(1)
                break
            if i == n - 1:
                print(3 - md)

          