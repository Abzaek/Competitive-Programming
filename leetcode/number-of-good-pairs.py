class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = {}
        ans = 0

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 0
            else:
                hashmap[i] += 1
        
        for i in hashmap.values():
            while i > 0:
                ans += i
                i-= 1
        return ans

        

        