class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) > len(b):
            x = len(a) - len(b)
            while x > 0:
                b = '0' + b
                x -= 1
        elif len(a) < len(b):
            x = len(b) - len(a)
            while x > 0:
                a = '0' + a
                x -= 1
        x = len(a)
        vai_1 = 0
        soma_bin = ''
        while x > 0:
            bin_r = int(a[x-1]) + int(b[x-1]) + vai_1
            if bin_r >= 2:
                bin_r = bin_r - 2
                vai_1 = 1
            else:
                vai_1 = 0
            soma_bin = str(bin_r) + soma_bin
            x -= 1
        if vai_1 == 1:
            soma_bin = str(vai_1) + soma_bin
        return soma_bin
###
if __name__ == '__main__':
    a = '1101'
    b = '111'
    g = Solution()
    print(g.addBinary(a, b))
