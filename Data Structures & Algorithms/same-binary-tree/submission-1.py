# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Iterative DFS to add nodes from both trees into a stack, pop two at a time,
        # and compare their values. Any mismatch returns False.
        # Time: O(n) / Space: O(n)

        # Mismatch if only one tree is empty
        if (p and not q) or (q and not p):
            return False

        # Match if both p and q are empty
        if not p and not q:
            return True

        stack = [p, q]
        while stack:
            p_node = stack.pop()
            q_node = stack.pop()

            # value mismatch
            if p_node.val != q_node.val:
                return False
            
            # if only one of p and q nodes have a left node, there is a structure mismatch
            if (p_node.left and not q_node.left) or (not p_node.left and q_node.left):
                return False
            # if both have left nodes, stack both
            elif p_node.left and q_node.left:
                stack.append(p_node.left)
                stack.append(q_node.left)
            
            # same logic with right children of p and q nodes
            if (p_node.right and not q_node.right) or (not p_node.right and q_node.right):
                return False
            elif p_node.right and q_node.right:
                stack.append(p_node.right)
                stack.append(q_node.right)
        
        return True
