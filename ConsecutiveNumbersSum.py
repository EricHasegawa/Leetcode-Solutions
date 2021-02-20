class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        if N == 1: return 1
        cnt, prev = 0, 0
        for i in range(N):
            sub = i + prev
            prev = sub
            div = i + 1
            Q, R = divmod(N - sub, div)
            if not Q:
                return cnt
            if not R:
                cnt += 1
