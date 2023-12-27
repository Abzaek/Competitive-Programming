class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ss = {}
        pntr = 0
        
        another = []
        for i in arr2:

            for j in range(pntr, len(arr1)):
                if arr1[j] in ss:
                    ss[arr1[j]] += 1
                else:
                    ss[arr1[j]] = 1

                if pntr < len(arr1) and arr1[j] == i:
                    arr1[j], arr1[pntr] = arr1[pntr], arr1[j]
                    pntr += 1

                    if i in ss:
                        del ss[i]
        for k in ss:
            for i in range(ss[k]//len(arr2)):
                another.append(k)

        for i in range(1, len(another)):
            p = i

            while p > 0 and another[p] < another[p - 1]:
                another[p], another[p - 1] = another[p - 1], another[p]
                p -= 1
        
        ans = arr1[:len(arr1) - len(another)]
        ans.extend(another)

        return ans
            