count = [0]
def masha(n, temp):
    if n <= 1:
        return temp
    n = n// 2
    left_side = masha(n, temp[:n])
    right_side = masha(n, temp[n:]) 
    return swap(left_side, right_side)
def swap(left, right):
    global count 
    if type(left) == bool or type(right) == bool:
        return False
    elif not left or not right:
        left.extend(right)
        return left
    elif left[0] > right[-1]:
        right.extend(left)
        count[0] += 1
        return right
    elif left[-1] > right[0]:
        count[0] = -1
        return False
    else:
        left.extend(right)
        return left


_ = int(input())
for i in range(_):
    m = int(input())
    arr = list(map(int, input().split()))
    count[0] = 0
    masha(m, arr)
    print(count[0])
