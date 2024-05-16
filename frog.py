N = int(input())
heights = list(map(int, input().split()))

dp = {N-1:0,N-2:abs(heights[N-1]-heights[N-2])}
if N==2:
    print(abs(heights[0] - heights[1]))
else:
    for i in range(N - 3, -1,-1):
        dp[i] = min(abs(heights[i]-heights[i+1])+dp[i+1],abs(heights[i] -heights[i+2])+dp[i+2])

    print(dp[0])
