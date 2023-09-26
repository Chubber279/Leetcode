class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        is_valid_dict = {")": "(", "]": "[", "}": "{"}
        stack = []
        for char in s:
            if char not in is_valid_dict:
                stack.append(char)
            else:
                if len(stack) > 0:
                    if stack[len(stack) - 1] == is_valid_dict[char]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0
    
    def bestSolution(self, s: str) -> bool:
        is_valid_dict = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char in is_valid_dict:
                top_element = stack.pop() if stack else "something"

                if top_element != is_valid_dict[char]:
                    return False
            else:
                stack.append(char)
        return not stack
    

solution = Solution()
print(solution.isValid("()"))
print(solution.isValid("()[]{}"))
print(solution.isValid("(]"))
print(solution.isValid("([)]"))
