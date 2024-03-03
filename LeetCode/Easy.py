# 704. Binary Search ==================================================================================================
# import math
#
#
# class Solution:
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         start = 0
#         end = len(nums) - 1
#         while start <= end:
#             mid = int(math.ceil((start + end) / 2))
#
#             guess = nums[mid]
#             if guess == target:
#                 return mid
#             elif guess > target:
#                 end = mid - 1
#             else:
#                 start = mid + 1
#         else:
#             return -1
