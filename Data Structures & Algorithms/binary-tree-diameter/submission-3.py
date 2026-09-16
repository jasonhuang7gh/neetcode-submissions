# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # DFS recursion to compute height of every subtree
        # For each node, recursively get the left height and right height
        # Height returned to parent = 1 + max(left_height, right_height)
        # Update the global max_diameter
        # Time: O(n) / Space: O(n) for recursive stack

        self.max_diameter = 0

        def dfs(node: Optional[TreeNode]) -> int:
            
            # Base case:
            if not node:
                return 0

            # Recursive case:
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            self.max_diameter = max(self.max_diameter, left_height + right_height)

            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.max_diameter


    #     # Brute force DFS recursion - get max diameter at every node
    #     # Time: O(n^2) / Space: O(n)
    #     # Base Case: No node, no children, no diameter
    #     if not root:
    #         return 0
    #     # At each node, compare its diameter to that of its left and right children
    #     # Calling max_depth function is O(n)
    #     diameter = self.max_depth(root.left) + self.max_depth(root.right)
    #     return max(diameter, \
    #         self.diameterOfBinaryTree(root.left), \
    #         self.diameterOfBinaryTree(root.right))

    # # Helper recursive function to find max depth of a node
    # def max_depth(self, node: Optional[TreeNode]) -> int:
    #     if not node:
    #         return 0
    #     return 1 + max(self.max_depth(node.left), self.max_depth(node.right))


        # # Initially I thought the diameter of the binary tree would be the max depth
        # # of its root's left node added to that of its right node, but the faulty 
        # # logic is assuming the longest path will always go through the root.
        # # Failed at 27/33 test case
        # def max_depth(node: Optional[TreeNode]) -> int:
        #     if not node:
        #         return 0
        #     return 1 + max(max_depth(node.left), max_depth(node.right))
        # return max_depth(root.left) + max_depth(root.right)