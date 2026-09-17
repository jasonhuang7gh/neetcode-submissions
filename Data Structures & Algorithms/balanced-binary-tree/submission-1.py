# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Problem with the DFS recursion is that the entire recursive stack has to be
        # executed before function can return False even if an inbalanced node has 
        # been found early. I will try to use a jank raise-exception method to 
        # immediately exit the recursive stack.
        # Time: O(n) / Space: O(n)

        class Found_Inbalance(Exception):
            def __init__(self, value):
                self.value = value

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            if abs(left_height - right_height) > 1:
                raise Found_Inbalance(False)
            return 1 + max(left_height, right_height)
        
        try:
            dfs(root)
        except Found_Inbalance as e:
            return e.value

        return True


        # # Brute force DFS recursion - get the left and right heights of the children
        # # of the node. If they differ by more than 1, set global boolean to False.
        # # Time: O(n) / Space: O(n) for recursive stack
        # self.is_balanced = True
        # # Compare heights of the children of the node, while returning node's own
        # # height to its parent.
        # def dfs(node: Optional[TreeNode]) -> int:
        #     if not node:
        #         return 0
        #     left_height = dfs(node.left)
        #     right_height = dfs(node.right)
        #     if abs(left_height - right_height) > 1:
        #         self.is_balanced = False
        #     return 1 + max(left_height, right_height)
        # dfs(root)
        # return self.is_balanced
