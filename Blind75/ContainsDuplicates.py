from collections import Counter     
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt = Counter()
        for item in nums:
            cnt[item] += 1
            if cnt[item] > 1:
                return True
        return False
