from collections import defaultdict
import math
for i in range(int(input())):
    a, b, l = list(map(int, input().split()))
    arr = []
    ans = 0
    Lookup = defaultdict(int)
    x = l
    while l % a == 0:
        Lookup[a] += 1
        l = l / a
    l = x
    while l % b:
        Lookup[b] += 1
        l = l / b
    for i in Lookup.values():
        ans += i
    print()
    