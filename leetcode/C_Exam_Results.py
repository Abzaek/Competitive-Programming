from collections import Counter
n = int(input())
s = list(map(int, input().split()))

lookup = Counter(s)
s.sort(key= lambda x: lookup[x])
_count = 0

l = 0
r = 1

while r < len(s):
    l = r

    while r < len(s) and s[r - 1] == s[r]:
        r += 1

    if r == l:
        _count += 1
    else:
        _count += min(r - l, lookup[s[l - 1]])
    r += 1

print(_count)

