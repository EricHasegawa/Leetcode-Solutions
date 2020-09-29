class Solution:
    def countBits(self, num: int) -> List[int]:
        arr = []
        for i in range(0, num + 1):
            b = bin(i)
            arr.append(b.count('1'))
        return arr
