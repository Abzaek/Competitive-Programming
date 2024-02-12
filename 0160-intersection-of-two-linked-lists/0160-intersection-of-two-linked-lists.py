# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        rabbit = headA
        tortoise = headB
        
        while rabbit and rabbit.next:
            rabbit = rabbit.next
        
        rabbit.next = headA
        pointer = rabbit
        rabbit = headB
        
        while rabbit and rabbit.next:
            tortoise = tortoise.next
            rabbit = rabbit.next.next
            
            if tortoise == rabbit:
                break
        if not rabbit or not rabbit.next:
            pointer.next = None
            return None
        rabbit = headB
        
        while rabbit != tortoise:
            tortoise = tortoise.next
            rabbit = rabbit.next
        pointer.next = None
        return rabbit
        
        