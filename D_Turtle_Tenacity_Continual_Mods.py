from collections import Counter
for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    lookup = Counter(arr)
    arr.sort()

    if arr[0] != arr[1]:
        print('YES')
    else:
        

    




