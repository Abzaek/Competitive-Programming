from collections import defaultdict
for i in range(int(input())):
    n = int(input())
    s = input()
    sSet = set(s)
    ans = float('inf')


    if 'a' not in sSet:
         r = len(s)
         l = -1
         ans = -1
    lookup = defaultdict(int)
    l = 0

    lookup[s[0]] += 1
    lookup[s[1]] += 1
    r = 2
    if r - l > 1 and lookup['a'] > lookup['b'] and lookup['a'] > lookup['c']:
            ans = min(r - l, ans)

    while r < len(s):
        lookup[s[r]] += 1
        while r - l > 2 and lookup['a'] > lookup['b'] and lookup['a'] > lookup['c'] and l < len(s):
            ans = min(r - l, ans)
            lookup[s[l]] -= 1
            l += 1
        r += 1
        while l < len(s) and s[l] != 'a' and r - l + 1 > 2:
            lookup[s[l]] -= 1
            l += 1
        while r < len(s) and (lookup['a'] < lookup['b'] or lookup['a'] < lookup['c']):
             lookup[s[r]] += 1
             r += 1
             
        if r < len(s) and l < len(s) and r - l > 1 and lookup['a'] > lookup['b'] and lookup['a'] > lookup['c']:
            ans = min(r - l + 1, ans)
    
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)