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


# 347. Top K Frequent Elements
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        data = {}
        for i in nums:
            if i in data:
                data[i] += 1
            else:
                data[i] = 1

        items = sorted(data.items(), key=lambda x: x[1], reverse=True)
        return [items[i][0] for i in range(k)]


# 137. Single Number II
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        digits = {}
        for i in nums:
            if i in digits and digits[i] == 2:
                digits.pop(i)
            elif i in digits:
                digits[i] += 1
            else:
                digits[i] = 1

        return list(digits)[0]
