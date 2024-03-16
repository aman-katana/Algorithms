# 7. Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        y = ''

        for i in str(x)[::-1]:
            y += i

        x = sign * int(y.strip('-'))

        if x < -2147483648 or x > 2147483647:
            return 0

        return x