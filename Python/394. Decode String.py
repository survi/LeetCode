class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        
        return self.multiply(s)
        
    def multiply(self, ss):
        if ss == "":
            return ss
        print '------------------------------'
        print 'multiply(self, ss)'
        outs = ""
        i = 0
        while i < len(ss):
            print 'i', i
            try:
                ni = float(ss[i])
            except:
                ni = -1
            if ni >= 0:
                j = i + 1
                while j < len(ss):
                    if ss[j] == '[':
                        break
                    else:
                        j += 1
                n = int(ss[i:j])
                nj = j - i
                print 'n', n, 'nj', nj
                j = i + 1 + nj
                k = 1
                while j < len(ss):
                    if ss[j] == '[':
                        k += 1
                    elif ss[j] == ']':
                        k -= 1
                    if k == 0:
                        break
                    j += 1
                print 'ss[i+2:j]', ss[i+1 + nj:j]
                print 'j', j
                m = j + 1
                print 'm',m
                outs += n * self.multiply(ss[i+1+nj:j])
                i = m
                print 'i', i
            else:
                outs += ss[i]
                i += 1
                print 'outs', outs
            
        print 'outs', outs
        print '------------------------------'
        return outs
        