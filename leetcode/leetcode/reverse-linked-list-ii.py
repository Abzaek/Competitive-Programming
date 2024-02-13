# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        head2 = ListNode()
        leftBoundary = head2
        head2.next = head
        curr = head2
        nxt = head2
        count = 0
        
        while count < right:
            if count == left - 1:
                leftBoundary = curr
            
            if count >= left and count < right:
                temp1 = nxt.next
                nxt.next = curr
                curr = nxt
                nxt = temp1
                
            if count < left:
                curr = curr.next
                nxt = curr.next
        
            count += 1
           
        leftBoundary.next.next = nxt
        leftBoundary.next = curr
        
        return head2.next