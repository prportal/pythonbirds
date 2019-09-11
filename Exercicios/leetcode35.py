class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for index, numero in enumerate(nums):
            if numero < target:
                pass
            elif numero == target:
                return(index)
            else:
                return(index)
        return(index+1)

##nums = [1,3,5,6]
##target = 5
nums = [1,3,5,6]
target = 1
s = Solution()
print(s.searchInsert(nums, target))
