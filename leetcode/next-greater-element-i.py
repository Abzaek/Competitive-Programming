class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = []
        lookup = {}
        
        for num in nums2:
            
            while stack and stack[-1] < num:
                lookup[stack[-1]] = num
                stack.pop()
                
                if not (stack and stack[-1] < num):
                    stack.append(num)

            else:
                stack.append(num)
        
        while stack:
            lookup[stack[-1]] = -1
            stack.pop()
        
        for num in nums1:
            ans.append(lookup[num])
        
        return ans
                
        