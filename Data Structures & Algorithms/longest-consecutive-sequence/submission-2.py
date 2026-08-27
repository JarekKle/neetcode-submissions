class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        length = 1
        max_length = 1
        last = nums[0]
        for i in range(1,len(nums)):
            if nums[i]==last+1:
                length+=1
                if length>max_length:
                    max_length = length
            else:
                length=1
            last = nums[i]
        return max_length
            