class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        s = s.lower()

        while start < end:
            if not s[start].isalnum():
                start += 1
            elif not s[end].isalnum():
                end -= 1
            elif s[start] != s[end]:
                print(s[start], s[end])
                return False
            else:
                start += 1
                end -= 1
            
        return True


solution = Solution()
print(solution.isPalindrome(s = "A man, a plan, a canal: Panama"))
print(solution.isPalindrome(s = "race a car"))
