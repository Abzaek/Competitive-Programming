# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        left, right = head, head.next
        
    
        while left and right:
            
            while right and right.val == left.val:
                right = right.next
                
            left.next = right
            left = left.next
            right = right.next if right else right
            
        return head