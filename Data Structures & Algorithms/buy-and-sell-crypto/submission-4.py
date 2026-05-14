class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        deltas = [0]
        for i in range(len(prices)-1):
            delta = max(prices[i+1:]) - prices[i]
            deltas.append(delta)
        maxvalue = max(deltas)
        if maxvalue >0:
            return maxvalue
        else:
            return 0