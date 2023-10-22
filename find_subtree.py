# from lintcode import (
#     TreeNode,
# )

from collections import deque
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


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

    def find_subtree01(self, root: TreeNode) -> TreeNode:
        # write your code here
        def check_subtree_sum (node, sum):
            
            if not node:
                return None, 0
            
            if node.left is None and node.right is None:
                return node, node.val
            
            if node.left:
                left_sum = check_subtree_sum (node.left, sum)

            if node.right:
                right_sum = check_subtree_sum(node.right, sum)

            curr_sum = int(left_sum[1]) + int(right_sum[1]) + int(node.val)
            print("curr_sum", curr_sum)
            return node, curr_sum
        
        max_sum = float("-inf")
        queue = deque([root])
        visited = []

        while queue:

            level_order = []
            for _ in range(len(queue)):
                node = queue.popleft()
                val = node.val
                level_order.append(node)

                if len(level_order) == 1:
                    node, curr_sum =  check_subtree_sum (root, 0)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        # node, curr_sum =  check_subtree_sum (root, 0)
        print("curr_sum", curr_sum)
        
        if curr_sum > max_sum:
            max_node = node
            max_sum = curr_sum
        print(max_node, max_sum)
        # return max_node


    def find_subtree_sum(self, root: TreeNode) -> TreeNode:
        self.max_sum = float("-inf")
        self.max_sum_node = None
        self.get_tree_sum(root)

        return self.max_sum_node

    def get_tree_sum(self, root: TreeNode) -> int:
        #1) all leafs are subtree, 
        #2) otherwise subtree_root needs to have at lease one child
        #3) use tree traversal here
        # if root:
        #     if root.left is not None or root.right is not None: #has at least one child
        #         return True
        #     elif root.left is None and root.right is None: # leaf
        #         return True

        # return False
        if root is None:
            return 0

        # if root.left is None and root.right is None: # this is the base case
        #     # print("root, root.val")
        #     # print(root, root.val)
        #     return root.val
    

        left_sum =  self.get_tree_sum(root.left)
        right_sum = self.get_tree_sum(root.right)
        print(root.val, left_sum, right_sum)
        curr_sum = root.val + left_sum + right_sum

        # if root.left is not None:
        #     left_sum =  self.get_tree_sum(root.left)
            
        
        # if root.right is not None:
        #     right_sum = self.get_tree_sum(root.right)
        

        # curr_sum = root.val + left_sum + right_sum

        if curr_sum > self.max_sum:
            self.max_sum = curr_sum
            self.max_sum_node = root

        return curr_sum


root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
# root.left.left.left = TreeNode(-4)
# root.left.left.right = TreeNode(-5)
new_solution = Solution()
result = new_solution.find_subtree_sum(root)
print("result", result)