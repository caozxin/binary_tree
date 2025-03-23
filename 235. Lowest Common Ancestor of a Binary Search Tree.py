# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # think from the prespective a node. first we check if root is a common ancester of p and q. 

        def dfs_checks (node, p, q, if_p_q):
            # print(node)
            if not node:
                return node # this is base case for dfs calls.

            if node.val == p.val:
                if_p_q[0] = True
            elif node.val == q.val:
                if_p_q[1] = True
            print(node.val, if_p_q)
            if if_p_q[0] and if_p_q[1]: 
                print("both true", node.val)
                return node
            if node.val < p.val and node.val < q.val: 
                dfs_checks(node.left, p, q, if_p_q) # you have to traversal both subtress. 
            elif node.val > p.val and node.val > q.val: 
                dfs_checks(node.right, p, q, if_p_q)
            else:
                return node 

        if_p_q = [False, False]
        dfs_checks (root, p, q, if_p_q)
