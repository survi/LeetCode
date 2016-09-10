class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        i = 0
        k = 0
        while i < len(data):
            print 'i', i
            print 'k', k
            if data[i] < 0:
                bincode = bin((1 << 30) + data[i])
            else:
                bincode = bin(data[i])
            code = bincode[2:][-8:]
            code = '0' * (8-len(code)) + code
            print code
            if code[0] == '0' and k == 0:
                i += 1
                continue
            elif code[0] == '0' and k != 0:
                return False
            elif code[0] == '1':
                if code[1] == '0' and k == 0:
                    return False
                elif code[1] == '0' and k != 0:
                    k -= 1
                    i += 1
                    continue
                elif code[1] == '1' and k != 0:
                    return False
                elif code[1] == '1' and k == 0:
                    if code[2] == '1':
                        if code[3] == '1':
                            if code[4] == '1':
                                return False
                            else:
                                k = 3
                        else:
                            k = 2
                    else:
                        k = 1
            i += 1
        if k == 0:
            return True
        else:
            return False