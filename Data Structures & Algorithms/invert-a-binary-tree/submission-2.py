# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # Breadth First Search with queue to iterate through nodes
        # Time: O(n) / Space: O(n)
        if not root:
            return None
        queue = deque([root])   # double-ended queue
        while queue:
            node = queue.popleft()
            temp = node.left
            node.left = node.right
            node.right = temp
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root


        # # Depth First Search with stack to iterate through nodes
        # # Time: O(n) / Space: O(n)
        # if not root:
        #     return None
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     temp = node.left
        #     node.left = node.right
        #     node.right = temp
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        # return root


        # # Depth First Search Recursion
        # # Time: O(n) / Space: O(n) for recursive stack
        # # Base Case: If root is None, return None
        # if not root:
        #     return None
        # # Recursive: Swap root's children
        # temp = root.left
        # root.left = root.right
        # root.right = temp
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root
    