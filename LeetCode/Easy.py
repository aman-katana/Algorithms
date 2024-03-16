# 704. Binary Search ==================================================================================================
# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         start, end = 0, len(nums) - 1
#
#         while start <= end:
#             mid = (start + end) // 2
#             guess = nums[mid]
#             if guess == target:
#                 return mid
#             elif guess > target:
#                 end = mid - 1
#             else:
#                 start = mid + 1
#         return -1

# 551. Student Attendance Record I
# class Solution:
#     def checkRecord(self, s: str) -> bool:
#         absent = late = 0
#         for i in s:
#             if i == 'A':
#                 absent += 1
#                 late = 0
#             elif i == 'L':
#                 late += 1
#             else:
#                 late = 0
#             if late == 3 or absent > 1:
#                 return False
#         else:
#             return True

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