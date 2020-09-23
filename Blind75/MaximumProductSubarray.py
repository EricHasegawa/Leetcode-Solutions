import numpy  
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        negatives = 0
        temp = max(nums)
        for num in nums:
            if num < 0:
                negatives += 1
        if negatives == 0 and 0 not in nums:
            return numpy.prod(nums)
        potentials = []
        curr_product = 1
        for num in nums:
            print(curr_product)
            if num > 0:
                curr_product = curr_product * num
            elif num == 0:
                potentials.append(curr_product)
                curr_product = 1
            else:
                negatives -= 1
                if curr_product < 0:
                    print("HEY")
                    curr_product = curr_product * num
                    if curr_product == 1:
                        potentials.append(1.1)
                if negatives >= 1:
                    potentials.append(curr_product)
                    curr_product = curr_product * num
                else:
                    potentials.append(curr_product)
                    curr_product = 1
        if max(potentials) == 1 or max(potentials) == 0:
            if 1.1 in potentials:
                return 1
            return temp
        else:
            if 1.1 in potentials:
                return 1
            return max(max(potentials), curr_product)
