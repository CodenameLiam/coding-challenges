# Given two binary strings a and b, return their sum as a binary string.

# 0 + 0 = 0
# 0 + 1 = 1
# 1 + 1 = 0 (no carry bit)
# 1 + 1 = 1 (with carry bit)

class Solution:
    def index_in_list(self, s: str, index: int) -> bool:
        return index < len(s)

    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        pointer = 0
        result = ""

        while pointer < len(a) or pointer < len(b) or carry != 0:
            _a = int(a[len(a) - pointer - 1]) if self.index_in_list(a, pointer) else 0
            _b = int(b[len(b) - pointer - 1]) if self.index_in_list(b, pointer) else 0

            value = _a + _b + carry

            if value == 2:
                value = 0
                carry = 1
            elif value == 3:
                value = 1
                varry = 1
            else:
                carry = 0

            result = str(value) + result

            pointer += 1

        return result


class SolutionBetter:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result = str(carry %2) + result
            carry //= 2

        return result

a = "11"
b = "1"
c = "1111"
d = "1111"

print(SolutionBetter().addBinary(c, d))