# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if not curr:
            return head
            
        theNext = curr.next
        curr.next = None
        while theNext:
            tempo = theNext
            theNext = theNext.next
            tempo.next = curr
            curr = tempo
            
            if theNext == None:
                head = curr
            
        
        
        
      
        return head
            
                
        