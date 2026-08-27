class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash = {}
        for i in range(len(nums)):
            num_hash[nums[i]] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num_hash and num_hash[diff] != i:
                return [i, num_hash[diff]]
        return []