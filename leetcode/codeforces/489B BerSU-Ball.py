n = int(input())
boys = list(map(int, input().split()))
m = int(input())
girls = list(map(int, input().split()))
boys.sort()
girls.sort()
b = 0
g = 0
pairs = 0

while b < n and g < m:
    if abs(boys[b] - girls[g]) > 1:
        if boys[b] > girls[g]:
            g += 1
        else:
            b += 1
    else:
        pairs += 1
        g += 1
        b += 1
        
print(pairs)

        