class Solution: 
    # def select(self, arr, i):
    #     # code here 
    
    def selectionSort(self, arr,n):
        #code here
        
        
        for i in range(n - 1):
            currMin = arr[i]
            index = i
            for j in range(i + 1, n):
                currIt = arr[j]
                if currIt <= currMin:
                    currMin = currIt
                    index = j
            arr[i], arr[index] = currMin, arr[i]
        return arr
        
