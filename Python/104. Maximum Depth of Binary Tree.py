# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 0 if root == None else max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1
    
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.maxd(root,0)
    
    def maxd(self, root, i = 0):
        if root == None:
            return i
        else:
            i += 1
            return max(self.maxd(root.left,i),self.maxd(root.right,i))