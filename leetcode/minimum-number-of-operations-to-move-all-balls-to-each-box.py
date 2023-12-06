class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0]*len(boxes) 

        j = 0
        while j < len(boxes):
            for i in range(len(boxes)):
                if boxes[i] == "1":
                    ans[j] += abs(j - i)
                
            j += 1
        return ans


        