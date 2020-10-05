class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        numCoins = 0
        i = len(coins) - 1
        while (amount > 0 and i >= 0):
            print(amount, i)
            if (amount <= coins[i]):
                amount -= coins[i]
                numCoins += 1
            else:
                i -= 1
        if amount != 0:
            return -1
        else:
            return numCoins
