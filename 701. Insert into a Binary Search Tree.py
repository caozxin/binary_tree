from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode, target: int) -> TreeNode:
        if not root:
            return TreeNode(target) # this is our exsit from recursion call! 

        if root.val < target:
            if not root.right: # if the node has no right child and the node.val < target val, TreeNode(val) should be its right child
                root.right = TreeNode(target)
            else: # if the node has another right child, we will continue searching 
                self.insertIntoBST(root.right, target)
        else:
            if not root.left: # if the node has no left child and node.val > target.val, TreeNode(val) should be its left child
                root.left = TreeNode(target)
            else:# if the node has another right child, we will continue searching 
                self.insertIntoBST(root.left, target)

        return root # here we return the updated node from child to parent
