class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        mult = 1
        zero_count = 0
        for number in nums:
            if number == 0:
                zero_count += 1
            else:
                mult = mult * number
        if zero_count >=2:
            return [0]*len(nums)
        for number in nums:
            if zero_count==1:
                if number==0:
                    result.append(mult)
                else:
                    result.append(0)
            else:
                result.append(int(mult/number))
        return result
                