class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pos = 0
        tam = len(nums)
        while pos < tam:
            if nums[pos] == val:
                nums.pop(pos)
                tam -= 1
            else:
                pos += 1
        return(len(nums))
##
nums = [0,1,2,2,3,0,4,2]
valor = 2
print(nums)
s = Solution()
print(s.removeElement(nums, valor))
print(nums)
