# 41. First Missing Positive
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums = [i for i in set(nums) if i > 0]
        nums.sort()
        if len(nums) < 1 or nums[0] != 1:
            return 1

        for i in range(len(nums) - 1):
            if nums[i] + 1 != nums[i + 1]:
                return nums[i] + 1
        return nums[-1] + 1