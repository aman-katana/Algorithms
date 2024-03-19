# 704. Binary Search ==================================================================================================
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            guess = nums[mid]
            if guess == target:
                return mid
            elif guess > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1


# 551. Student Attendance Record I
class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = late = 0
        for i in s:
            if i == 'A':
                absent += 1
                late = 0
            elif i == 'L':
                late += 1
            else:
                late = 0
            if late == 3 or absent > 1:
                return False
        else:
            return True


# 977. Squares of a Sorted Array
class Solution(object):
    def sortedSquares(self, nums, do=True):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = [i ** 2 for i in nums] if do else nums
        if len(nums) < 2:
            return nums
        else:
            mid = nums.pop(len(nums) // 2)
            left = [i for i in nums if i <= mid]
            right = [i for i in nums if i > mid]
            return self.sortedSquares(left, do=False) + [mid] + self.sortedSquares(right, do=False)


# 58. Length of Last Word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip(' ')
        end = len(s) - 1
        for i in range(end, -1, -1):
            if s[i] == ' ':
                return end - i

        return end + 1


# 28. Find the Index of the First Occurrence in a String
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return - 1

        for i in range(len(haystack)):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1


# 66. Plus One
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[-1] != 9:

            digits[-1] += 1
            return digits
        elif len(digits) > 1 and digits[-2] != 9:

            digits[-2] += 1
            digits[-1] = 0
            return digits

        digits = int(''.join(map(str, digits))) + 1

        return list(map(int, str(digits)))


# 169. Majority Element
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


# 268. Missing Number
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return nums[-1] + 1
