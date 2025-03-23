# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs_checks(node, p, q):
            if not node:
                return None
            
            # If both p and q are smaller, LCA must be in the left subtree
            if node.val > p.val and node.val > q.val:
                return dfs_checks(node.left, p, q)
            
            # If both p and q are larger, LCA must be in the right subtree
            if node.val < p.val and node.val < q.val:
                return dfs_checks(node.right, p, q)
            
            # If we reach here, it means node is the split point (LCA)
            return node 

        return dfs_checks(root, p, q)

