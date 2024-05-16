n = int(input())
n_arr = list(map(int, input().split()))
q = int(input())


n_arr.sort()

for i in range(q):
    a = int(input())
    l = -1
    r = n
    
    while l + 1 < r:
        mid = l + (r - l)//2
        
        if n_arr[mid] <= a:
            l = mid
        else:
            r = mid
    print(l + 1)