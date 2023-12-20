class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        '''

        for i in range(n):
            iterate over each other element and check if they are equal:
                check if i*j %k == 0:
                    increase count by one
    
        [3, 1, 2, 2, 2, 1, 3], k = 2
        
        '''
        count = 0
        
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if (i*j)%k == 0:
                    if nums[i] == nums[j]:
                        count += 1
        
        return count