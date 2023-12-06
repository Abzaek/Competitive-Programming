class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        hshmp1 = {}
        hshmp2 = {}

        for i in range(len(list1)):
            hshmp1[list1[i]] = i
        
        for i in range(len(list2)):
            hshmp2[list2[i]] = i
        
        for i in hshmp1:
            if i in hshmp2 and len(ans) == 0:
                ans.append(i)
            elif i in hshmp2:
                if hshmp1[ans[0]] + hshmp2[ans[0]] > hshmp1[i] + hshmp2[i]:
                    ans[0] = i
                elif hshmp1[ans[0]] + hshmp2[ans[0]] == hshmp1[i] + hshmp2[i]:
                    ans.append(i)
        
        return ans

         
        