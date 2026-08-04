# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Find the middle of the linkedlist using slow and fast pointers.
        # Reverse the second half of the list before merging.
        # Time: O(n) / Space: O(1)

        # Fast pointer moves two nodes per iteration, slow pointer just one.
        # Fast pointer always at twice the node distance of slow pointer.
        slow = head
        fast = head.next

        # So when fast pointer reaches the end, slow pointer is at midpoint.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Slow pointer marks the head of second half of linkedlist. Reverse it.
        curr = slow.next
        prev = slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Prev is the head of the reversed linkedlist. Merge it with first half.
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2


        # Brute force - Use a list to hold each ListNode for later construction
        # Time: O(n) / Space: O(n)
        # listnode_list = []
        # while head is not None:
        #     listnode_list.append(head)
        #     head = head.next
        # i, j = 0, len(listnode_list) - 1
        # while i < j:
        #     listnode_list[i].next = listnode_list[j]
        #     i += 1
        #     if i >= j:
        #         break
        #     listnode_list[j].next = listnode_list[i]
        #     j -= 1  
        # listnode_list[i].next = None