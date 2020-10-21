class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in range(0, len(digits)):
            s += str(digits[i])
        ret = int(s) + 1
        return list(str(ret))
