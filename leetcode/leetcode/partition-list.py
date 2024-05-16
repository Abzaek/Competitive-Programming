# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smallerNodes = ListNode()
        largerNodes = ListNode()
        
        smallerTail = smallerNodes
        largerTail = largerNodes
        
        
        while head:
            if head.val < x:
                smallerTail.next = head
                smallerTail = smallerTail.next
            else:
                largerTail.next = head
                largerTail = largerTail.next
            head = head.next
            
        smallerTail.next = largerNodes.next
        largerTail.next = None
        
        return smallerNodes.next
            