# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortoise = head
        rabbit = head 
        
        while rabbit and rabbit.next:
            rabbit = rabbit.next.next
            tortoise = tortoise.next
            
            if rabbit == tortoise:
                break
        if not rabbit or not rabbit.next:
            return None
        rabbit = head
        
        while rabbit != tortoise:
            rabbit = rabbit.next
            tortoise = tortoise.next
        return rabbit
        
        