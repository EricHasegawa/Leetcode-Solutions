class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        curr_max = 0
        while (i < j):
            curr_height = min(height[i], height[j])
            curr_width = j - i
            temp = curr_height * curr_width
            if temp > curr_max:
                curr_max = temp
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
                
        return curr_max
