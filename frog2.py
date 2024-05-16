N, k= map(int, input().split())
heights = list(map(int, input().split()))

dp = {N-1:0}

if N==2:
    print(abs(heights[0] - heights[1]))
else:
    for i in range(N-2, N-k-1, -1):
        mn = float('inf')
        for j in range(i+1, N):
            mn = min(mn, abs(heights[i]-heights[j])+dp[j])
        dp[i] = mn

    for i in range(N - k-1, -1,-1):
        mn = float('inf')
        for j in range(i+1, i+k+1):
            # print(j)
            mn = min(mn, abs(heights[i] - heights[j])+dp[j])
        dp[i] = mn
# print(dp)
    print(dp[0])
