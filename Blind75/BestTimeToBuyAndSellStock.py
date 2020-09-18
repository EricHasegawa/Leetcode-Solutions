class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        curr_max = 0
        potentials = [curr_max]
        comp = prices[-1]
        i = len(prices) - 2
        while (i >= 0):
            temp = prices[i]
            if comp - temp > curr_max:
                curr_max = comp - temp
                potentials.append(curr_max)
            if temp > comp:
                comp = temp
            i -= 1
        return max(potentials)
