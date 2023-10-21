

# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

from collections import deque

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer

    description: Given a binary tree, find its maximum depth. --> depth == how many levels the tree has
    The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

    """
    def max_depth(self, root: TreeNode) -> int:
        # write your code here
        
        queue = deque([root])
        visited = []
        counter = 0
        if not root:
            return 0
        
        while queue:
            level_order = []
            counter +=1 
            for _ in range(len(queue)):

                node = queue.popleft()
                val = node.val

                # print(val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return counter

        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.left.left.left = TreeNode(-4)
root.left.left.right = TreeNode(-5)
new_solution = Solution()
result = new_solution.max_depth(root)
print("result", result)