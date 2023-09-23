class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I": 1, "V": 5, "X":10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prev = ""
        value = 0
        s = s.upper()
        for index, letter in enumerate(s):
            if prev == "":
                prev = letter
                if index == len(s) - 1:
                    value += roman_dict[prev]
                continue
            if roman_dict[prev] < roman_dict[letter]:
                value += (roman_dict[letter] - roman_dict[prev])
                prev = ""
            else:
                if index == len(s) - 1:
                    value += roman_dict[prev] + roman_dict[letter]
                else:
                    value += roman_dict[prev]
                prev = letter
        return value
    
    def bestSolution(self, s: str) -> int:
        roman_dict = {"I": 1, "V": 5, "X":10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prev_value = 0
        result = 0
        for letter in s[::-1]:
            curr_value = roman_dict[letter]
            if curr_value >= prev_value:
                result += curr_value
            else:
                result -= curr_value
            prev_value = curr_value
        return result

solution = Solution()
print(solution.romanToInt("IV"))