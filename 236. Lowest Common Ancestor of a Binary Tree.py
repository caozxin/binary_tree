# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs_checks(node, p, q):
            if not node: # exit strategy/base case if we reach leaf node
                return None
            
            # If root matches either p or q, return root
            if node == p or node == q:
                return node
            
            left = dfs_checks(node.left, p, q)
            right = dfs_checks(node.right, p, q)

            # If both left and right are not null, root is the LCA
            if left and right:
                return node
            
            # If only one side returns a valid node, return that node
            return left if left else right

        return dfs_checks(root, p, q)
