from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = Counter()
        for num in nums:
            c[num] += 1
        to_remove = []
        for i in range(0, len(nums)):
            if c[nums[i]] > 1:
                to_remove.append(i)
                c[nums[i]] -= 1
        for index in sorted(to_remove, reverse=True):
            del nums[index]
        return len(nums)
