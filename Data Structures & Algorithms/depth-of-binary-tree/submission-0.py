# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # Depth First Search recursion. While traversing down, keep track of
        # current depth and compare it to max depth at the end of each path.
        # Time: O(n) / # Space: O(n) for recursive stack

        self.max_depth = 0

        def dfs(node: Optional[TreeNode], curr_depth: int) -> None:
            if node:
                curr_depth += 1
                dfs(node.left, curr_depth)
                dfs(node.right, curr_depth)
            else:
                self.max_depth = max(self.max_depth, curr_depth)
        
        dfs(root, 0)
        return self.max_depth