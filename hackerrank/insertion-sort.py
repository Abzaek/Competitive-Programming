def insertionSort1(n, arr):
    # Write your code here
    unSorteNum = arr[n - 1] if arr[n - 1] < arr[n - 2] else None
    for i in range(1, n):
        if arr[n - i - 1] > unSorteNum:
            arr[n - i] = arr[n - i - 1]
            print(' '.join(map(str, arr)))
        else:
            arr[n - i] = unSorteNum
            print(' '.join(map(str, arr)))
            
        
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
