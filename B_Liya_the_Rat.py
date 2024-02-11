s = input()
m = int(input())
n = len(s)

p_sum = [0]*n

for i in range(n - 1):
    if s[i] == s[i + 1]:
        p_sum[i] = 1
for i in range(1, n):
    p_sum[i] = p_sum[i - 1] + p_sum[i]

for i in range(m):
    a,b = list(map(int, input().split()))

    if a == 1:
        print(p_sum[b - 2])
        continue

    print(p_sum[b - 2] - p_sum[a - 2])



