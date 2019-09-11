class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        print(s)
        if s == 0:
            rtype = False
            return(rtype)
        rtype = True
        expressao_aberta = []
        for caract in s:
            if caract not in ('(', '[', '{', ')', ']', '}'):
                return(False)
            if caract in ('(', '[', '{'):
                expressao_aberta.append(caract)
            if caract == ')':
                if len(expressao_aberta) == 0:
                    return(False)
                if expressao_aberta[len(expressao_aberta) - 1] == '(':
                    expressao_aberta.pop(len(expressao_aberta) - 1)
                else:
                    rtype = False
            if caract == ']':
                if len(expressao_aberta) == 0:
                    rtype = False
                elif expressao_aberta[len(expressao_aberta) - 1] == '[':
                    expressao_aberta.pop(len(expressao_aberta) - 1)
                else:
                     rtype = False
            if caract == '}':
                if len(expressao_aberta) == 0:
                    rtype = False
                elif expressao_aberta[len(expressao_aberta) - 1] == '{':
                    expressao_aberta.pop(len(expressao_aberta) - 1)
                else:
                    rtype = False
        if len(expressao_aberta) == 0:
            return(rtype)
        else:
            return(False)

##expressao = ('{[(())][]}{}')
##expressao = ('{%}')
##expressao = ('{[(})]')
expressao =(']()')
s = Solution()
print(s.isValid(expressao))
