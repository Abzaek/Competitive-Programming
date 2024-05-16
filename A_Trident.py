for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = [0]

    for j in range(1, n):

        if len(ans) == 1:
            if arr[j] < arr[ans[-1]]:
                ans.pop()
                ans.append(j)
            elif arr[j] > arr[ans[-1]]:
                ans.append(j)

        elif len(ans) == 2:
            if arr[j] < arr[ans[-1]]:
                ans.append(j)
            elif arr[j] > arr[ans[-1]]:
                ans.pop()
                ans.append(j)
        if len(ans) == 3:
            break
    
    if len(ans) == 3:
        print('YES')
        for i in range(len(ans)):
            ans[i] += 1
        print(' '.join(map(str, ans)))
    else:
        print('NO')     