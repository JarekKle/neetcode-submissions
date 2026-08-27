class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow_i = 0
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[slow_i] = nums[i]
                k += 1
                slow_i += 1
        return k
        