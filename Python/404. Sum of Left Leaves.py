# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        self.countleft(root, False)
        return self.count
        
    def countleft(self, root, isLeft):
        if root:
            if isLeft and root.left == None and root.right == None:
                self.count += root.val
            else:
                if root.left:
                    self.countleft(root.left, True)
                if root.right:
                    self.countleft(root.right, False)