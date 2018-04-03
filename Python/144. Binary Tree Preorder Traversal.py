# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        else:
            return []

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        visitlist = []
        self.visit(root,visitlist)
        return visitlist
        
    def visit(self, root,visitlist):
        if root:
            visitlist.append(root.val)
        
            self.visit(root.left, visitlist)
        
            self.visit(root.right,visitlist)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        visitlist = []
        waitlist = []
        while root or waitlist:
            if root:
                visitlist.append(root.val)
                waitlist.append(root.right)
                root = root.left
            else:
                root = waitlist.pop()
                
        return visitlist
        