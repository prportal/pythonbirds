class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        pos_i = 1
        nums_soma = []
        tam = len(nums)
#        for index, x in enumerate(nums):
        while pos_i <= tam:
            nums_soma.append(sum(nums[0: pos_i]))
            pos_i += 1
        pos_i = 0

        hsum = max(nums_soma)
        print(nums_soma)
#
        while pos_i < len(nums_soma):
            pos_f = pos_i +1
            while pos_f < len(nums_soma):
                soma = nums_soma[pos_f] - nums_soma[pos_i]
                if soma > hsum:
                    hsum = soma
                pos_f += 1
            pos_i +=1
        return(hsum)
##
#nums = [-2,1,-3,4,-1,2,1,-5,4]
#nums = [1, 2]
nums = [-2, 1]
s = Solution()
print(s.maxSubArray(nums))
