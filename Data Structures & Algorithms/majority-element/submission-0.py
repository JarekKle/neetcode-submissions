class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_hash = {}
        major = []
        for num in nums:
            maj_hash[num] = maj_hash.get(num, 0) + 1
        return max(maj_hash, key=maj_hash.get)