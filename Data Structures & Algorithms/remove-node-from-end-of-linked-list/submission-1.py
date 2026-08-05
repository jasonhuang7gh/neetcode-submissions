# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Brute force - append nodes in a list to find nth node from end
        # Time: O(n) / Space: O(n)

        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        sz = len(nodes)
        
        # Edge case where node removed is the first node
        if n == sz:
            head = head.next

        # Edge case where node removed is the last node
        elif n == 1:
            nodes[(sz - 1) - 1].next = None
        
        # Rest of cases where node removed is between two nodes
        else:
            nodes[(sz - 1) - n].next = nodes[(sz - 1) - n + 2]
        
        return head