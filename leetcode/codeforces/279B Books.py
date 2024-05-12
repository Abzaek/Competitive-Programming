n, t = map(int, input().split())
arr = list(map(int, input().split()))

l = 0 
r = 0
_sum =0
_max = 0

while r < n:
    _sum += arr[r]
    while _sum > t:
        _sum -= arr[l]
        l += 1
    _max = max(_max, r - l + 1)
    r += 1
        
    
    
print(_max)
