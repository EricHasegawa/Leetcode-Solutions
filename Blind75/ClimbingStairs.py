class Solution:
    
    def climbStairs2(self, n, dp):
        if dp[n] != 0:
            return dp[n]
        if n == 0 or n == 1:
            return 1
        else:
            result = Solution.climbStairs2(self,n - 1, dp) + Solution.climbStairs2(self, n - 2, dp)
            dp[n] = result
            return result
        
    def climbStairs(self, n: int) -> int:
        dp = [0] *  (n + 1)
        return Solution.climbStairs2(self, n, dp)
             
