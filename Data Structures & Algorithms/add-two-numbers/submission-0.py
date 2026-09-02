# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1_list, l2_list = [], []
        while l1:
            l1_list.append(l1.val)
            l1 = l1.next
        while l2:
            l2_list.append(l2.val)
            l2 = l2.next
        
        l1_num, l2_num = "", ""
        for i in range(len(l1_list) - 1, -1, -1):
            l1_num += str(l1_list[i])
        for i in range(len(l2_list) - 1, -1, -1):
            l2_num += str(l2_list[i])
        
        sum_num = str(int(l1_num) + int(l2_num))
        sum_head = ListNode()
        curr = sum_head
        for i in range(len(sum_num) - 1, 0, -1):
            curr.val = sum_num[i]
            curr.next = ListNode()
            curr = curr.next
        
        curr.val = sum_num[0]
        curr.next = None
        return sum_head