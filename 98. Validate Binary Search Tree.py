# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, val=0, left=None, right=None):
 #         self.val = val
 #         self.left = left
 #         self.right = right
class Solution:
     def isValidBST(self, root: Optional[TreeNode]) -> bool:
         
         def inorder_validation(node, pre_state):
             if node is None:
                 return True # if we finish traversal and all validation checks out, then we should return true
 
             if not inorder_validation(node.left, pre_state): # we only move forward if left subtree is valid
                print(" left false!")
                return False

             if pre_state and node.val <= pre_state[-1]:
                print("false!")
                return False
                     
             pre_state.append(node.val)

             return inorder_validation(node.right, pre_state) # we continue to traversal to right until node is null. If the right subtree is invalid, we will return False right away. 

         return inorder_validation(root,[])
