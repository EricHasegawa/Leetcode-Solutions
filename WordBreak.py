class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        size = len(s)
        dp = [False] * (size + 1)
        dp[0] = True
        for i in range(0, size + 1):
            for j in range(0, i):
                if dp[j] and (s[j:i] in wordDict):
                    dp[i] = True
                    break
        print(dp)
        return dp[size]
