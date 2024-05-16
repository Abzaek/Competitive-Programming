# zero one
for i in range(int(int(input()))):
    n = int(input())
    s = input()
    l = 0
    r = n - 1

    while r > l and s[l] != s[r]:
        r -= 1
        l += 1
    print(r - l + 1)

# for i in range(int(input())):
#     arr = list(map(int, input().split()))
#     leul = arr[0]
#     riri = arr[0]
#     ans = arr[0]

#     for j in range(1, len(arr)):
#         if j == 1:
#             riri -= min(riri, arr[j])
#             ans += min(riri, arr[j])
#             arr[j] -= min(riri, arr[j])
#         elif j == 2:
#             leul -= min(riri, arr[j])
#             ans += min(riri, arr[j])
#             arr[j] -= min(riri, arr[j])
            

    