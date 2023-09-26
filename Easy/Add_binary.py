class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a) - 1
        len_b = len(b) - 1
        carry = 0
        result = ""

        while len_a >= 0 or len_b >= 0 or carry != 0:
            if len_a >= 0:
                carry += int(a[len_a])
                len_a -= 1
            if len_b >= 0:
                carry += int(b[len_b])
                len_b -= 1
            result = str(carry % 2) + result
            carry = carry // 2
        return result    


solution = Solution()
answer = solution.addBinary(a = "1010", b = "1011")
print(answer)