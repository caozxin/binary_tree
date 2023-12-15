from typing import (
    List,
)
from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def search_range(self, root: TreeNode, k1: int, k2: int) -> List[int]:
        # write your code here
        if not root:
            return []

        result_list = []

        def dfs(root: TreeNode, k1: int, k2: int):
            if not root:
                return
            print(root.val)
            if root.val < k1:
                dfs(root.right, k1, k2)
            elif root.val > k2:
                dfs(root.left, k1, k2)
            else:
                dfs(root.left, k1, k2)
                dfs(root.right, k1, k2)
                result_list.append(root.val)
                
            if not root.left and not root.right:
                # result_list.append(root.val)
                return
        def dfs00(root: TreeNode, k1: int, k2: int):
            if not root:
                return
            dfs(root.left, k1, k2)
            dfs(root.right, k1, k2)
            if root.val >= k1 and root.val <= k2:
                result_list.append(root.val)
                
            if not root.left and not root.right:
                # result_list.append(root.val)
                return
        dfs(root, k1, k2)
        result_list.sort()
        return result_list
