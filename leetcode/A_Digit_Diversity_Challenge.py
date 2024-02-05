from collections import Counter
l, r = list(map(int, input().split()))
flag = True

for i in range(l, r+1):
    lookup = Counter(str(i))
    _count = 0

    for j in lookup:
        if lookup[j] > 1:
            break
        _count += 1
    
    if _count == len(lookup):
        print(i)
        flag = False
        break

if flag:
    print(-1)

        
