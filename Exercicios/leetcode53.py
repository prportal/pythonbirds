class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hsum = max(nums)
        pos_i = 0
        while pos_i < len(nums):
            pos_f = pos_i +2
            while pos_f <= len(nums):
                soma = sum(nums[pos_i: pos_f])
                if soma > hsum:
                    hsum = soma
                pos_f += 1
            pos_i +=1
        return(hsum)
##
nums = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
print(s.maxSubArray(nums))
