class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []

        for i in range(len(arr)):
            _max = float('-inf')
            index = 0

            for j in range(len(arr) - i):
                if arr[j] >= _max:
                    _max = arr[j]
                    index = j
            arr[:index + 1] = arr[:index + 1][::-1]
            arr[:len(arr) - i] = arr[:len(arr) - i][::-1]

            ans.append(index + 1)
            ans.append(len(arr) - i)
        print(arr)
        return ans


                
               
            


            


        