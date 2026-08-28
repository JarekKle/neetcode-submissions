class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                remain = 0 - nums[i]
                j_k_sum = nums[j] + nums[k]
                if j_k_sum > remain:
                    k -= 1
                elif j_k_sum < remain:
                    j += 1
                else:
                    if [nums[i],nums[j],nums[k]] not in result:
                        result.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j -1] and j < k:
                        j += 1
        return result