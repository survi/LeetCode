class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        dv = { 'a':True, 'e':True, 'o':True, 'u':True, 'i':True,'A':True, 'E':True, 'O':True, 'U':True, 'I':True}
        lsv = []
        lsvn = []
        rsl = list(s)
        for i in range(len(s)):
            ts = s[i]

            if dv.get(ts,0):

                lsv.append(s[i])
                lsvn.append(i)


        rlsv = lsv[::-1]


        j = 0
        for i in lsvn:
            rsl[i] = rlsv[j]
            j = j + 1

        return "".join(rsl)

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        dv = { 'a':True, 'e':True, 'o':True, 'u':True, 'i':True,'A':True, 'E':True, 'O':True, 'U':True, 'I':True}
        lsv = []
        lsvn = []
        rsl = list(s)
        i = 0 
        j = len(rsl) - 1

        while i < j:
            while not dv.get(rsl[i],False) and i < j:
                i = i + 1

            while not dv.get(rsl[j],False) and i < j:
                j = j - 1 

            if i < j:
                rsl[i], rsl[j] = rsl[j], rsl[i]
                i = i + 1
                j = j - 1


        return "".join(rsl)