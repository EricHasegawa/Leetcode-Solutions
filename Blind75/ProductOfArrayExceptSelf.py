class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)
        left[0] = 1
        for i in range(1, len(nums)):
            left[i] = nums[i - 1] * left[i - 1]
            
        right[len(nums) - 1] = 1
        for i in reversed(range(len(nums) - 1)):
            right[i] = nums[i + 1] * right[i + 1]
        ret = [0] * len(nums)
        for i in range(len(nums)):
            ret[i] = left[i] * right[i]
        return ret
