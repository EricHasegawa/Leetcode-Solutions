class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) == 1:
            if s[-1] == "V":
                return 5
            elif s[-1] == "L":
                return 50
            elif s[-1] == "D":
                return 500
            elif s[-1] == "V":
                return 1000
            elif s[-1] == "I":
                return 1
            elif s[-1] == "X":
                return 10
            elif s[-1] == "C":
                return 100
            elif s[-1] == "M":
                return 1000
            else:
                return "Invalid Input"
        i = 0
        total = 0
        while i < len(s) - 1:
            if s[i] == "I":
                if s[i + 1] == "V":
                    total += 4
                    i += 2
                elif s[i + 1] == "X":
                    total += 9
                    i += 2
                else:
                    total += 1
                    i += 1
            elif s[i] == "X":
                if s[i + 1] == "L":
                    total += 40
                    i += 2
                elif s[i + 1] == "C":
                    total += 90
                    i += 2
                else:
                    total += 10
                    i += 1
            elif s[i] == "C":
                if s[i + 1] == "D":
                    total += 400
                    i += 2
                elif s[i + 1] == "M":
                    total += 900
                    i += 2
                else:
                    total += 100
                    i += 1
            else:
                if s[i] == "V":
                    total += 5
                    i += 1
                elif s[i] == "L":
                    total += 50
                    i += 1
                elif s[i] == "D":
                    total += 500
                    i += 1
                elif s[i] == "M":
                    total += 1000
                    i += 1
                else:
                    return "Invalid Input"
        second_last = s[-2]
        if second_last == "I" and (s[-1] == "V" or s[-1] == "X"):
            return total
        elif second_last == "X" and (s[-1] == "L" or s[-1] == "C"):         
            return total
        elif second_last == "C" and (s[-1] == "D" or s[-1] == "M"):  
            return total
        else:
            if s[-1] == "V":
                total += 5
            elif s[-1] == "L":
                total += 50
            elif s[-1] == "D":
                total += 500
            elif s[-1] == "V":
                total += 1000
            elif s[-1] == "I":
                total += 1
            elif s[-1] == "X":
                total += 10
            elif s[-1] == "C":
                total += 100
            elif s[-1] == "M":
                total += 1000
            else:
                return "Invalid Input"
            return total
