class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 0
        while pos < len(nums) -1:
            if nums[pos] == nums[pos + 1]:
                nums.pop(pos+1)
            else:
                pos += 1
        return(len(nums))

#nums = [0,0,1,1,1,2,2,3,3,4]
nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution()
print(s.removeDuplicates(nums))
print(nums)
