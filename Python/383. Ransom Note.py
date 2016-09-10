class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if ransomNote == "":
            return True
        sd = {}
        for s in ransomNote:
            if sd.get(s, False):
                sd[s] += 1
            else:
                sd[s] = 1
        for s in magazine:
            if sd.get(s, False):
                sd[s] -= 1
                if sd[s] <= 0:
                    sd.pop(s)
                    if len(sd.keys()) <= 0:
                        return True
        if len(sd.keys()) > 0:
            return False


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if ransomNote == "":
            return True
        sd = {}
        sdm = {}
        for s in ransomNote:
            if sd.get(s, False):
                sd[s] += 1
            else:
                sd[s] = 1
        for s in magazine:
            if sdm.get(s, False):
                sdm[s] += 1
            else:
                sdm[s] = 1
        for s in sd.keys():
            if sdm.get(s, 0) < sd.get(s,0):
                return False
        return True

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
      for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True



class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in set(ransomNote):
            if len(ransomNote.split(i)) > len(magazine.split(i)):
                return False
        return True


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

