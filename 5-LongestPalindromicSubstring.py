class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxPalindrome = ""
        for i in range(0, len(s)):
            odd = Solution.expandMid(self, s, i , i)
            even = Solution.expandMid(self, s, i, i + 1)
            if len(odd) > len(even):
                curr = odd
            else:
                curr = even
            if len(curr) > len(maxPalindrome):
                maxPalindrome = curr
        return maxPalindrome
            
    def expandMid(self, s: str, left: int, right: int) -> int:
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        return s[left + 1:right]
