# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, min_val, max_val):
            # empty nodes are always valid
            if not root:
                return True

            if not (min_val < root.val < max_val):
                return False

            # see notes below
            print('min_val, max_val')
            print(min_val, max_val)
            return dfs(root.left, min_val, root.val) and dfs(root.right, root.val, max_val)
            
            # min_val is updated when checking the right subtree → dfs(root.right, root.val, max_val).
            # max_val is updated when checking the left subtree → dfs(root.left, min_val, root.val).
            # This ensures that every node satisfies BST conditions as we traverse recursively.

        return dfs(root, -inf, inf)  # root is always valid
