class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        str_int = ''
        ## transforma lista de inteiros em um número inteiro
        for n in digits:
            str_int = str_int + str(n)
        inteiro = int(str_int) + 1
 ##
        new_digits = []
        for dig in str(inteiro):
            new_digits.append(int(dig))

        return new_digits
###
if __name__ == '__main__':
    digits = [1, 2, 9]
    digits = [9, 9, 9]
    digits = [9]
    g = Solution()
    print(g.plusOne(digits))
