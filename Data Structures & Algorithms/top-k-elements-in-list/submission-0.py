from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_hash = defaultdict(int)
        for num in nums:
            k_hash[num] += 1
        k_sorted = dict(sorted(k_hash.items(), key=lambda item: item[1], reverse=True))
        return list(k_sorted.keys())[0:k]