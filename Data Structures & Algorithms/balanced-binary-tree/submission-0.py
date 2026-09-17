# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Brute force DFS recursion - get the left and right heights of the children
        # of the node. If they differ by more than 1, set global boolean to False.
        # Time: O(n) / Space: O(n) for recursive stack

        self.is_balanced = True

        # Compare heights of the children of the node, while returning node's own
        # height to its parent.
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            if abs(left_height - right_height) > 1:
                self.is_balanced = False
            
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.is_balanced


