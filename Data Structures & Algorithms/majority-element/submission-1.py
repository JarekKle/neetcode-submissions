class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_hash = {}
        max_count = 0
        val = 0
        for num in nums:
            maj_hash[num] = maj_hash.get(num, 0) + 1
            if maj_hash[num] > max_count:
                max_count = maj_hash[num]
                val = num
        return val