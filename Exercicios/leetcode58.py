class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos = len(s)
        tam = pos
        last_word = ''
        carac = ''
        if ' ' not in s:
            return len(s)
        while pos >= 0:
            carac = s[pos-1]
            if carac ==' ':
                if last_word != '':
                    pos = 0
            else:
     #           last_word = s[pos-1: tam]
                last_word = last_word + carac
            pos -= 1
        if last_word != '':
            print(last_word)
            return len(last_word)
        else:
            return(0)
#
if __name__ == '__main__':
    s = "Hello world"
#    s = "a "
    g = Solution()
    print(g.lengthOfLastWord(s))
