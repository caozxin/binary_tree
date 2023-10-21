from typing import (
    List,
)



# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
             we will sort your return value in output
    """
    def binary_tree_paths(self, root: TreeNode) -> List[str]:
        # write your code here

        def path_finder( node, path, paths):
            print(node, path, paths)
            if not node:
                return 

            if not node.left and not node.right:
                paths.append('->'.join([str(each_node.val) for each_node in path]))
                print(paths)
                return paths

            path.append(node.left) # this is the current path
            path_finder(node.left, path, paths)
            path.pop()

            path.append(node.right) # this is the current path
            path_finder(node.right, path, paths)
            path.pop()

        path = [root]
        paths = []
        path_finder(root, path, paths)
        return paths
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(2)
# root.left.left.left = TreeNode(-4)
# root.left.left.right = TreeNode(-5)
new_solution = Solution()
result = new_solution.binary_tree_paths(root)
print("result", result)