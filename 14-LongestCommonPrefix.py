class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        longest_substring = ""
        for i in range(0, len(strs[0])):
            
            end = False
            
            try:
                curr = strs[0][i]
            except IndexError:
                return longest_substring
            
            for sub in strs:
                try:
                    if sub[i] != curr:
                        end = True
                except IndexError:
                    return longest_substring
                
            if end:
                return longest_substring
            else:
                longest_substring += curr    
        return longest_substring
