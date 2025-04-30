# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def inorderTraversal(node):
            result = []
            if node:
                result.extend(inorderTraversal(node.left))
                result.append(node.val)
                result.extend(inorderTraversal(node.right))

            return result

        return len(set(inorderTraversal(root))) == 1
