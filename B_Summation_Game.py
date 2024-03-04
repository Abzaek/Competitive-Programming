for z in range(int(input())):
    n, k, x = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    sum_1 = 0
    sum_2 = 0
    temp = arr[: n- k]
    for i in range(len(temp)):
        sum_1 += arr[i]
    
    pointer = len(temp) - 1

    while pointer >= 0 and pointer >= len(temp) - x:
        sum_2 -= temp[pointer]
        pointer -= 1
    sum_2 += sum_1

    

    print(max(sum_2,sum_1))