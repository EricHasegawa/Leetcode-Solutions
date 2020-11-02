from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = lo = 0
        counts = collections.Counter()
        for hi in range(len(s)):
            counts[s[hi]] += 1
            
            # count of most common character in window
            max_char_n = counts.most_common(1)[0][1]
            
            # slide window as necessary
            while (hi - lo - max_char_n + 1 > k):
                counts[s[lo]] -= 1
                
                lo += 1
            res = max(res, hi - lo + 1)
        return res
