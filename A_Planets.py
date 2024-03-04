
from collections import Counter
for i in range(int(input())):
    n, c = list(map(int, input().split()))
    orbits = list(map(int, input().split()))
    count = 0
    lookup = Counter(orbits)

    for orbit in lookup.keys():
        if lookup[orbit] >= c:
            count += c
            continue
        count += 1
    print(count)