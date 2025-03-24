# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import ast
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # print(root)
        def dfs_decode(root, res_list): 
            if not root:
                return res_list.append('N') # we need to mark the leaf node
            # print(root.val)
            res_list.append(str(root.val))
            # res_list.append(root.val)

            left = dfs_decode(root.left, res_list)
            right = dfs_decode(root.right, res_list)
            
            return res_list

        decoded = dfs_decode(root, [])
        # print(decoded)
        return str(decoded)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if not data or data == 'None':
            return None

        data_lst = ast.literal_eval(data)  # Convert string back to list

        def dfs_decode():
            if not data_lst:
                return None
            value = data_lst.pop(0)  # Take the first element and remove it. Similar to dequeue(). 
            if value == 'N':
                return None
            node = TreeNode(int(value))  # Convert value back to TreeNode
            node.left = dfs_decode()  # Recur for left subtree
            node.right = dfs_decode()  # Recur for right subtree
            return node

        return dfs_decode()
        
            
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
    # Codec.serialize(root, [])
