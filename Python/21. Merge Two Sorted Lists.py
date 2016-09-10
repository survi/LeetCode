# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.compLN(l1, l2)
            
    def compLN(self, l1, l2):
        if (l1 != None) or (l2 != None):
            if l1 == None or (l2 != None and l1.val >= l2.val):
                templ = l2
                templ.next = self.compLN(l1, l2.next)
            else:
                templ = l1
                templ.next = self.compLN(l1.next, l2)
            return templ
        else:
            return None
    

                    