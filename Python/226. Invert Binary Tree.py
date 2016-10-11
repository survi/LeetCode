# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.inv(root)
        return root
    
    def inv(self,root):
        if root:
            root.left, root.right = root.right, root.left
            self.inv(root.left)
            self.inv(root.right)
        