
n = int(input())

temp = list(map(int, input().split()))
temp.sort()
p = 0
count = 0
r = 0

while r < n:
    if temp[r] >= p:
        count += 1
        p += temp[r]
    r += 1

print(count)


