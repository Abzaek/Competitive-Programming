N = int(input())
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

dp = [[0 for i in range(3)] for i in range(N)]
dp[-1] = [a for a in arr[-1]]
# print(arr)
# print(dp)
def inbound(x):
    return x > -1 and x<3
direction = [(-1, 1), (1, 1)]

for i in range(N-2, -1,-1):
    for j in range(3):
        
        mn = float('-inf')

        for d in direction:
            x,y = d
            x+=j
            y+=i
            mn = max(mn, dp[y][x%3])

        dp[i][j] = mn + arr[i][j]
_max = float('-inf')

for a in dp[0]:
    _max = max(a, _max)
print(_max)


