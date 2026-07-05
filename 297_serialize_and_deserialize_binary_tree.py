# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        ans = ""
        def preorder(node):
            nonlocal ans

            if node is None:
                ans+="#" + ","
                return
            
            ans += str(node.val) + ","
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return ans

        

    def deserialize(self, data):

        array = data.split(",")
        self.index = 0

        def dfs():

            if self.index >= len(array):
                return 
            
            if array[self.index] == "#":
                self.index+=1
                return None
            
            node = TreeNode(array[self.index])
            self.index+=1
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()
        

            
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))