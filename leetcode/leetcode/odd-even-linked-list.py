# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        
        odd = ListNode()
        oddTail = odd
        even = ListNode()
        evenTail = even
        
        curr = head
        count = 1
        
        while curr:
            if count % 2 != 0 or count == 1:
                oddTail.next = curr
                oddTail = oddTail.next
            else:
                evenTail.next = curr
                evenTail = evenTail.next
            count += 1
            curr = curr.next
            
        oddTail.next = even.next
        evenTail.next = None
        return odd.next
        