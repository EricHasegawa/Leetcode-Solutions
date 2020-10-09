class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        to_close = []
        for char in s:
            if char in ["[", "(", "{"]:
                to_close.append(char)
            else:
                if len(to_close) == 0:
                    return False
                elif char == "]" and to_close[-1] == "[":
                    to_close.pop()
                elif char == ")" and to_close[-1] == "(":
                    to_close.pop()
                elif char == "}" and to_close[-1] == "{":
                    to_close.pop()
                else:
                    return False
        if len(to_close) != 0:
            return False
        else:
            return True
