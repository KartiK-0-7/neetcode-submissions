class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min=prices[0]
        curr_profit=0
        for i in range(len(prices)):
            curr_min=min(prices[i],curr_min)
            p=prices[i]-curr_min
            curr_profit=max(curr_profit,p)
        return curr_profit