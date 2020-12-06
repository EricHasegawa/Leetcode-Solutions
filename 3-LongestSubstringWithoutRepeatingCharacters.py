class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        total_max = 0
        curr_max = 0
        curr_chars = []
        for i in range(0, len(s)):
            if s[i] in curr_chars:
                if curr_max > total_max:
                    total_max = curr_max
                curr_chars = [s[i]]
                j = i - 1
                while j > 0:
                    if s[j] != s[i]:
                        curr_chars.append(s[j])
                        j -= 1
                    else:
                        break
                curr_max = len(curr_chars)
            else:
                curr_chars.append(s[i])
                curr_max += 1
        if len(curr_chars) > total_max:
            return len(curr_chars)
        else:
            return total_max
