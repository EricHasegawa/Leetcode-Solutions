# Slow Solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        hashmap =  {}
        # Create a dictionary where keys are numbers, and values are index of those numbers
        zeroes = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                zeroes += 1
            hashmap[nums[i]] = i
        if zeroes >= 3:
            triplets.append([0,0,0])
        print(hashmap) 
        for i in range(0, len(nums)):
            target = 0 - nums[i]
            for j in range(0, len(nums)):
                if j == i:
                    continue
                else:
                    complement = target - nums[j]
                    if complement in hashmap and hashmap[complement] != j and hashmap[complement] != i:
                        temp = [nums[i], nums[j], complement]
                        got = False
                        for sublist in triplets:
                            if (all(x in sublist for x in temp)):
                                got = True
                                break
                        if not got:
                            triplets.append(temp)
        return triplets
        
        
        # Proper Solution
