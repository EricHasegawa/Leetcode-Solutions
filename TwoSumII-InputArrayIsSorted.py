class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(numbers)):
            if numbers[i] in d:
                d[numbers[i]].append(i)
            else:
                d[numbers[i]] = [i]
        
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in d:
                if d[complement][0] == i:
                    continue
                if i < d[complement][0]:
                    return [i + 1, d[complement][0] + 1]
                else:
                    return [d[complement][0] + 1, i + 1]
        return “oops"
