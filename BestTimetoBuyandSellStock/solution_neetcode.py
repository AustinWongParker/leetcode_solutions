class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0,1 # left is buying, right is selling
        maxProfit = 0

        while right < len(prices):

            # profitable transaction?
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right # if right pointer is lower price than left
            right += 1

        return maxProfit