import collections
def solve():
    n = int(input())
    arr = input()
    lookup = {0: 1}

    sm = 0
    cnt = 0
    for i, item in enumerate(arr):
        sm += int(item)
        if sm - i - 1 in lookup:
            cnt += 1
        lookup[sm - i - 1] = 1
        
    print(cnt)





tc = int(input())

for i in range(tc):
    solve()