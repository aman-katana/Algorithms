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


# 34. Find First and Last Position of Element in Sorted Array
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start = 0
        end = len(nums)
        while start < end:
            mid = (start + end) // 2

            if nums[mid] == target:
                # Если target найден идём в лево и право циклом for
                # и проверяем равняются ли значения target и когда перестают быть равным обрываем цикл
                first = second = -1
                for i in range(mid, -1, -1):
                    if nums[i] != target:
                        break
                    first = i
                for i in range(mid, len(nums)):
                    if nums[i] != target:
                        break
                    second = i
                return [first, second]

            elif target < nums[mid]:
                end = mid
            elif target > nums[mid]:
                start = mid + 1

        return [-1, -1]


# 151. Reverse Words in a String
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])


# 287. Find the Duplicate Number
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        digits = {}
        for n in nums:
            if digits.get(n):
                return n
            digits[n] = 1


# 189. Rotate Array
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        if k == 0:
            return
        elif len(nums) > k:
            nums[:] = nums[-k:] + nums[:(len(nums) - k)]
        else:
            for i in range(k):
                nums.insert(0, nums.pop(-1))

# 378. Kth Smallest Element in a Sorted Matrix
class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        new_matrix = []
        for item in matrix:
            new_matrix.extend(item)

        new_matrix.sort()
        return new_matrix[k - 1]
