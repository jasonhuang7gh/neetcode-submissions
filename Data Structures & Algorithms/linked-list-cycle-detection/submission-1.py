# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
            
        val_set = set()
        while(head.next != None):
            if head.val in val_set:
                return True
            val_set.add(head.val)
            head = head.next
        
        return False