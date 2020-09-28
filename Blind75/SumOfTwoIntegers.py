class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b != 0:
            sum_ = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a, b = sum_, carry
        if (a >> 31) & 1: 
            return ~(a^mask)
        else:
            return a
