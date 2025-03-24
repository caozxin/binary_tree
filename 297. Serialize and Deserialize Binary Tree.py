# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs_decode(root, res_list): 
            if not root:
                return res_list.append('N') # we need to mark the leaf node
            print(root.val)
            # res_list.append(str(root.val))
            res_list.append(root.val)

            left = dfs_decode(root.left, res_list)
            right = dfs_decode(root.right, res_list)
            
            return res_list

        print(dfs_decode(root, []))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
    # Codec.serialize(root, [])
