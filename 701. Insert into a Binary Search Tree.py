from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if root is None:
        #     return TreeNode(val) # If tree is empty, return new node as root
        
        def search(node, val):
            if node is None:
                return TreeNode(val)  # Create new node when reaching a leaf
            if node.val > val:
                node.left = search(node.left, val)  # Keep searching
            elif node.val < val:
                node.right = search(node.right, val)  # Keep searching
            return node  # Return the node to maintain structure

        search(root, val)  # Start inserting from the root
        return root  # Return modified root
