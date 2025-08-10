def orderAgnosticBS(arr, target ) -> int:
  start = 0
  end = len(arr) - 1
  
  is_asc = arr[end] > arr[start]

  while start <= end:
    middle = start + (end - start)//2
    
    if arr[middle] == target:
      return middle
        
    if is_asc:
      if arr[middle] > target:
        end = middle - 1
      else:
        start = middle + 1
    else:
      if arr[middle] < target:
        end = middle - 1
      else:
        start = middle + 1
  
  return -1

arr = [-1, 0, 2, 3, 4, 5, 6, 78]
print(orderAgnosticBS(arr, 0), 1, arr[1])
	  
