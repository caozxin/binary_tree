# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def inorder(node, pre_state):
            if node is None:
                # print(pre_state)
                return True

            if not inorder(node.left, pre_state): # we could move forward if left subtree is valid
                return False
            # print("curr: ", node.val, pre_state)
            if pre_state and node.val <= pre_state[-1]:
                    print("false!")
                    return False
                    
            pre_state.append(node.val)
            # pre_state = node.val
            return inorder(node.right, pre_state)
                # return False
            # print("af: ", node.val)
            # return node
            # print(pre_state)
            # return True

        return inorder(root,[])

