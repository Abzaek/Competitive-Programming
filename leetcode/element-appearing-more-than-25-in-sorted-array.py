class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        '''
        i will have two pointers
        increase the right pointer by one until there is a change in number
        when there is a change in number i will check if the difference of the two pointers is greater than 25% of len(arr) if found i will return that number, else i will move my left pointer to the last element of the previous number and continue increasing the right pointer
        '''
        l = -1
        r = 0

        while r < len(arr):
            if r - l > 0.25*len(arr):
                return arr[l + 1]
            if arr[r] != arr[r + 1]:
                l = r
            r += 1
