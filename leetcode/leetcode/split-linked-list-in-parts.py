# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        length = 0
        ans = []
        head2 = ListNode()
        head2.next = head
        curr = head
        while curr:
            length += 1
            curr = curr.next
        curr = head
        
        reminder = length % k
        number = length // k
        
        while curr:
            count = 1
            tempHead = curr
            
            while count < number and curr:
                curr = curr.next
                count += 1
                
            if reminder:
                if number != 0:
                    
                    curr = curr.next
                    reminder -= 1
            if curr:
                temp = curr.next
                curr.next = None
                curr = temp
            ans.append(tempHead)
            
        while len(ans) < k:
            ans.append(None)
        return ans
            
            
        
        