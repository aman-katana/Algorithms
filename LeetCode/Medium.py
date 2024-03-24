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


# 75. Sort Colors
class Solution:
    def sortColors(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first = []
        second = []
        for i in nums:
            if i == 0:
                first.append(i)
            elif i == 1:
                second.insert(0, i)
            else:
                second.append(i)

        nums[:] = first + second


# 81. Search in Rotated Sorted Array II
class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        max_index = -1
        last = nums[0]
        for i in range(len(nums)):
            if nums[i] < last:
                max_index = i - 1
                break
            last = nums[i]
        nums = nums[max_index + 1:] + nums[0: max_index + 1]
        start = 0
        end = len(nums)
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid + 1

        return False
