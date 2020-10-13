class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        indexes = []
        for i in range(0, len(nums)):
            if nums[i] == val:
                indexes.append(i)
        for index in sorted(indexes, reverse=True):
            del nums[index]
        return len(nums)
