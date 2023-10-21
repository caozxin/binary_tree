from collections import deque


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.

    description: Given a binary tree, determine if it is height-balanced.
    For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

    Examples:
    tree = {1,2,3} --> True
    tree = {1,#,2,3,4} --> False

    """

    def build_tree_from_list(self, lst):
        if not lst:
            return None

        root = TreeNode(lst[0])
        stack = [root]
        index = 1

        while stack:
            node = stack.pop()

            # Process the left child
            if index < len(lst) and lst[index] != "#":
                left_val = int(lst[index])
                node.left = TreeNode(left_val)
                stack.append(node.left)
            index += 1

            # Process the right child
            if index < len(lst) and lst[index] != "#":
                right_val = int(lst[index])
                node.right = TreeNode(right_val)
                stack.append(node.right)
            index += 1

        return root

    def build_tree_from_list02(self, arr):
        # Check if the list is empty
        if not arr:
            return None

        # Create a TreeNode for the first element in the list
        root = TreeNode(arr[0])

        # Recursively build the left and right subtrees
        if len(arr) > 1:
            root.left = self.build_tree_from_list(arr[1:])
        if len(arr) > 2:
            root.right = self.build_tree_from_list(arr[2:])

        return root

    def view_tree_bfs(self,root: TreeNode):
        queue = deque([root])
        visited = []
        counter = -1

        while queue:
            level = "           "
            counter += 1
            print(level, "level: ", counter )

            for _ in range(len(queue)):
                node = queue.popleft()
                val = node.val
                if val not in visited:
                    visited.append(val)
                else:
                    break
                print(val)

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                
    
    def count_height(self, root: TreeNode) -> int:
        print
    def is_balanced(self, root: TreeNode) -> bool:
        # write your code here
        print
        

new_solution = Solution()
tree = list({1,2,3})
tree = [1,"#",2,3,4]
built_tree = new_solution.build_tree_from_list(tree)
# print(built_tree)
view_graph = new_solution.view_tree_bfs(built_tree)