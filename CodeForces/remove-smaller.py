def remove_smaller(n, arr):
    count = [0] * (max(arr) + 1)
    sortedA = []
    counter = 0

    for a in arr:
        count[a] += 1

    for c in range(len(count)):
        while count[c] > 0:
            sortedA.append(c)
            count[c] -= 1

    for i in range(len(sortedA) - 1):
        if sortedA[i + 1] - sortedA[i] <= 1:
            counter += 1

    return "YES" if counter == len(arr) - 1 else "NO" 



t = int(input(""))

while t:
    n = int(input(""))
    arr = [int(x) for x in input("").split(" ")]
    print(remove_smaller(n, arr))
    t -= 1
            
            
