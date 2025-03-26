# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs_checks(node, p, q, if_p_q):
            if not node:
                return None
            
            # # If both p and q are smaller, LCA must be in the left subtree
            # if node.val == p.val:
            #     if_p_q[0] = 'true'
            # elif node.val == q.val:
            #     if_p_q[1] = 'true'
            
            left = dfs_checks(node.left, p, q, if_p_q)
            right = dfs_checks(node.right, p, q, if_p_q)
            
            # If we reach here, it means node is the split point (LCA)
            if node.val == p.val:
                if_p_q[0] = 'true'
            elif node.val == q.val:
                if_p_q[1] = 'true'
            print(node.val, if_p_q)

            return node 

        if_p_q = ['false', 'false']

        return dfs_checks(root, p, q, if_p_q)
