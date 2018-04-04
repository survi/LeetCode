class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2 == 1:
            return False
        sdict={}
        sdict['('] = ')'
        sdict['{'] = '}'
        sdict['['] = ']'
        stack = []
        for sub in s:
            if sub in '({[':
                stack.append(sub)
            else:
                if len(stack) > 0 and sub == sdict[stack.pop()]:
                    continue
                else:
                    return False
        return stack == []
        
            
                
 class Solution(object):
     def isValid(self, s):
         """
         :type s: str
         :rtype: bool
         """
         if len(s)%2 == 1:
             return False
         sdict={}
         sdict['('] = ')'
         sdict['{'] = '}'
         sdict['['] = ']'
         slist = list(s)
         i = 0
         while i >= 0 and i < len(slist) - 1:
             if sdict.get(slist[i], None) is None:
                 return False
             elif sdict[slist[i]] == slist[i+1]:
                 slist.pop(i+1)
                 slist.pop(i)
                 i = max(i - 1,0)
             else:
                 i = i + 1
         return len(slist) == 0        
        
        
 class Solution(object):
     def isValid(self, s):
         """
         :type s: str
         :rtype: bool
         """
         sdict={}
         sdict['('] = ')'
         sdict['{'] = '}'
         sdict['['] = ']'        
         if len(s)%2 == 1:
             return False
         i = 0
         while i >= 0 and i < len(s)-1:
             if sdict.get(s[i], None) is None:
                 return False
             elif sdict[s[i]] == s[i+1]:
                 if i+1 == len(s)-1:
                     s = s[:i]
                 else:
                     s = s[:i] + s[i+2:]
                 i = i - 1
                 if i < 0:
                     return True
             else:
                 i = i + 1
         if len(s) == 0:
             return True
         return False
        