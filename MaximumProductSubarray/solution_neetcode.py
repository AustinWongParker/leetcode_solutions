#this is returning incorrect on leetcode, but this is the same code in neetcode vid

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        currentMin, currentMax = 1, 1

        for n in nums:
            if n == 0:
                currentMin, currentMax = 1, 1
                continue
            temp = currentMax * n
            currrentMax = max(n * currentMax, n * currentMin, n)
            currrentMin = min(temp, n * currentMin, n)
            result = max(result, currentMax)
        return result
