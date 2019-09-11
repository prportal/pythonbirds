class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        retorno = 0
        if needle not in haystack:
            return(-1)
        if len(needle) == 0:
            return(0)
        pos = len(needle) - 1
        while pos <= len(haystack):
            if needle in haystack[0: pos]:
                retorno = pos - len(needle)
                pos = len(haystack) + 1 # condição para sair do while
            else:
                pos += 1
        return(retorno)

##haystack = 'dfpcvtalc'
##needle = 'alc'
haystack = 'aaa'
needle = 'a'
s = Solution()
print(s.strStr(haystack, needle))
