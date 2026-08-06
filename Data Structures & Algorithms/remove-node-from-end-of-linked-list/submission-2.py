# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Use two pointers to keep track of the end of list and (n+1)th from end node.
        # We keep track of (n+1)th from end node, so we can set (n+1)th from end to 
        # point to (n-1)th from end node, which effectively removes nth from end node.
        # Time: O(n) / Space: O(1)

        # Edge case - only one node in list
        if head.next is None:
            head = None

        else:
            # Assign the pointers. Set node_j to be n nodes away from node_i
            node_i, node_j = head, head
            for i in range(n):
                node_j = node_j.next

            # Edge case - if head node is to be removed, there is no (n+1)th from end node
            if node_j is None:
                head = head.next

            # Edge case - if end node is to be removed
            elif n == 1:
                while(node_i.next.next):
                    node_i = node_i.next
                node_i.next = None

            # Rest of cases where node removed is between two nodes
            else:
                node_j = node_j.next
                # At this point, node_i is (n+1) nodes away from node_j. 
                # Iterate until node_j is None.
                while(node_j):
                    node_i = node_i.next
                    node_j = node_j.next
                # node_i is at (n+1)th from end position now. Remove nth node.
                node_i.next = node_i.next.next

        return head


        # # Brute force - append nodes in a list to find nth node from end
        # # Time: O(n) / Space: O(n)
        # nodes = []
        # curr = head
        # while curr:
        #     nodes.append(curr)
        #     curr = curr.next
        # sz = len(nodes)
        # # Edge case where node removed is the first node
        # if n == sz:
        #     head = head.next
        # # Edge case where node removed is the last node
        # elif n == 1:
        #     nodes[(sz - 1) - 1].next = None
        # # Rest of cases where node removed is between two nodes
        # else:
        #     nodes[(sz - 1) - n].next = nodes[(sz - 1) - n + 2]
        # return head