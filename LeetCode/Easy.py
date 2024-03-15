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
class Solution(object):
    def checkRecord(self, s: str):
        """
        :type s: str
        :rtype: bool
        """
        absent = 0
        late = 0
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
