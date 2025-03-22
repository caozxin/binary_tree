from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val) # this is our exsit from recursion call! 

        if root.val < val:
            if not root.right: # if the node has no right child and the node.val < target val, TreeNode(val) should be its right child
                root.right = TreeNode(val)
            else: # if the node has another right child, we will continue searching 
                self.insertIntoBST(root.right, val)
        else:
            if not root.left: # if the node has no left child and node.val > target.val, TreeNode(val) should be its left child
                root.left = TreeNode(val)
            else:# if the node has another right child, we will continue searching 
                self.insertIntoBST(root.left, val)

        return root # here we return the updated node from child to parent
