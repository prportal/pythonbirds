class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        seq = ['1', '11']
        pos_lista = 1
        while pos_lista < n:  ## varrendo a lista
            nova_seq = ''
            count = 0
            for index, x in enumerate(seq[pos_lista]):  ## varrendo o string
                if index == 0:
                    str_ant = x
                    count = 1
                elif str_ant == x:
                    count += 1
                else:
                    nova_seq = nova_seq + str(count)
                    nova_seq = nova_seq + str_ant
                    str_ant = x
                    count = 1
##
            nova_seq = nova_seq + str(count)
            nova_seq = nova_seq + str_ant
            seq.append(nova_seq)
            pos_lista += 1
        return(seq[n-1])

n = 7
s = Solution()
print(s.countAndSay(n))
