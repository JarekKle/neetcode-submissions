class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if len(numbers) == 2:
                return [1, 2]
            left = i+1
            right = len(numbers)-1
            while left <= right:
                j = (left + right) // 2
                if numbers[i] + numbers[j] > target:
                    right = j-1
                elif numbers[i] + numbers[j] < target:
                    left = j+1
                else:
                    return [i+1, j+1]