class Solution:
    
    def diffWaysToCompute(self, input: str) -> List[int]:
        import re
        chars = re.findall(r'(\d+|\W)', input)
        return self.comp(chars)
    
    def comp(self, exp):
        if len(exp) == 1:
            return [int(exp[0])]
        
        results = []
        
        for i in range(1, len(exp), 2):
            l_vals = self.comp(exp[:i])
            r_vals = self.comp(exp[i + 1:])
        
            for l_val in l_vals:
                for r_val in r_vals:
                    if exp[i] == '+':
                        results += [l_val + r_val]
                    elif exp[i] == '-':
                        results += [l_val - r_val]
                    else:
                        results += [l_val * r_val]
        return results
