class Solution:
    def maxArea(self, height: list[int]) -> int:
        res = 0
        l, r = 0, len(height)-1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            #if height[l] > height[r]: # could delete this code 
                #r -= 1
            else: # both heights are equal
                r -= 1

        return res