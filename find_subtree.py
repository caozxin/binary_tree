# from lintcode import (
#     TreeNode,
# )
from typing import (
    List,
)

# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

        # if self.val is None:
        #     self.val = val
        # elif self.val < val and self.right is None:
        #     self.right = val
        # elif self.val > val and self.left is None:
        #     self.left = val

    def printInorder(self, root):
        if root:
            # First recur on left child
            self.printInorder(root.left)
    
            # Then print the data of node
            print(root.val, end=" "),
    
            # Now recur on right child
            self.printInorder(root.right)


class Solution:
    """
    @param root: the root of binary tree
    @return: the maximum weight node

    description: Given a binary tree, find the subtree with maximum sum. Return the root of the subtree.

    Input:
    {1,-5,2,0,3,-4,-5}
    Output:3
    Explanation:
    The tree is look like this:
        1
    /   \
    -5     2
    / \   /  \
    0   3 -4  -5
    The sum of subtree 3 (only one node) is the maximum. So we return 3.

    Input:
    {1}
    Output:1
    Explanation:
    The tree is look like this:
    1
    There is one and only one subtree in the tree. So we return 1.
    """

    def find_subtree(self, root: TreeNode) -> TreeNode:
        self.min_sum = float("inf")
        self.min_sum_root = None
        self.subtree_sum(root)
        return self.min_sum_root


    def subtree_sum (self, root): 
    # we should use dfs here to first traverse all nodes
        if not root:
            return 0

        left_sum = self.subtree_sum(root.left)
        right_sum = self.subtree_sum(root.right)
        
        total_sum = root.val + right_sum + left_sum

        if total_sum < self. min_sum:
            self.min_sum = total_sum
            self.min_sum_root = root

        return total_sum
    
    def print_subtree(self, root): # this function can print subtree for each node using DFS
        if root is None:
            return []

        subtree = [root.val]

        if root.left:
            left_subtree = self.print_subtree(root.left)
            subtree.extend(left_subtree) # in python, extend() concatenates the first list with another list/iterable.

        if root.right:
            right_subtree = self.print_subtree(root.right)
            subtree.extend(right_subtree)

        print("Subtree for node", root.val, ":", subtree)

        return subtree
    
    def find_subtree02(self, root: TreeNode) -> TreeNode:
                # path = [root] # this is our stack here. Remember in python, stack == list()
        self.min_sum = float("inf")
        self.min_sum_root = None
        
        # return self.min_sum_root
        

        def print_subtree(root):
            if root is None:
                return []

            subtree = [root.val]

            if root.left:
                left_subtree = print_subtree(root.left)
                subtree.extend(left_subtree)

            if root.right:
                right_subtree = print_subtree(root.right)
                subtree.extend(right_subtree)

            print("Subtree for node", root.val, ":", subtree)
            curr_sum = sum(subtree)

            if curr_sum < self.min_sum:
                self.min_sum = curr_sum
                self.min_sum_root = root

            return subtree

            
        print_subtree(root)
        return self.min_sum_root
# new_solution = Solution()
# input_vals = {1,-5,2,0,3,-4,-5}
# root = TreeNode(1)
# root.left = TreeNode(-5)
# root.right = TreeNode(2)
# root.left.left = TreeNode(0)
# root.left.right = TreeNode(3)
# root.printInorder(root)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(-5)
    root.right = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.left.left.left = TreeNode(-4)
    root.left.left.right = TreeNode(-5)
 
    # Function call
    print("Inorder traversal of binary tree is")
    # root.printInorder(root)
    new_solution = Solution()
    new_solution.find_subtree(root)




