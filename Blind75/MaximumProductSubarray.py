class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        positive = nums[0]
        negative = nums[0]
        result = nums[0]
        for num in nums[1:]:
            positive, negative = max(num, positive * num, negative * num), min(num, positive * num, negative * num)
            result = max(result, positive)
        return result
