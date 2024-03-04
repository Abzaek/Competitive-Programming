def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = a[0]
    mn = min(0, a[0])
    sum_val = a[0]

    for i in range(1, n):
        if abs(a[i]%2) == abs(a[i - 1]%2):
            mn = 0
            sum_val = 0
        sum_val += a[i]
        ans = max(ans, sum_val - mn)
        mn = min(a[i], sum_val)
    print(ans)
tc = int(input())
for t in range(tc):
    solve()
