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


# 136. Single Number
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        digits = {}
        for i in nums:
            if digits.get(i):
                del digits[i]
            else:
                digits[i] = 1

        return list(digits.keys())[0]


# 344. Reverse String
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]


# 242. Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = "abcdefghijklmnopqrstuvwxyz"
        for l in letters:
            if s.count(l) != t.count(l):
                return False
        return True


# 217. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) == len(nums)


# 258. Add Digits
class Solution:

    def addDigits(self, num: int) -> int:
        num = str(num)

        while len(num) > 1:
            num = str(sum(map(int, num)))

        return int(num)


# 500. Keyboard Row
class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        f, s, th, = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        ans = []
        for word in words:
            w = set(word.lower())
            if w <= f or w <= s or w <= th:
                ans.append(word)
        return ans


# 283. Move Zeroes
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = [i for i in nums if i != 0] + [i for i in nums if i == 0]


# 387. First Unique Character in a String
class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars_dict = {}
        for char in s:
            if char in chars_dict:
                chars_dict[char] += 1
            else:
                chars_dict[char] = 1

        for i in range(len(s)):
            if chars_dict.get(s[i]) == 1:
                return i

        return -1


# 121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0

        min_index = 0
        max_prof = 0
        for i in range(len(prices)):
            if prices[i] < prices[min_index]:
                min_index = i
            elif i > min_index and prices[i] - prices[min_index] > max_prof:
                max_prof = prices[i] - prices[min_index]

        return max_prof if max_prof > 0 else 0


# 557. Reverse Words in a String III
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        return ' '.join([item[::-1] for item in s])


# 14. Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        min_len = len(strs[0])

        for i in range(len(strs)):
            min_len = min(min_len, len(strs[i]))

        ans = ""
        for len_s in range(1, min_len + 1):
            prefix = strs[0][:len_s]
            ok = True

            for i in range(len(strs)):
                if strs[i][:len_s] != prefix:
                    ok = False
                    break

            if ok:
                ans = prefix
            else:
                break

        return ans


# 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        cost = {
            '(': 1,
            '[': 2,
            '{': 3,

            '}': -3,
            ']': -2,
            ')': -1
        }
        for i in range(len(s)):
            x = cost[s[i]]

            if x > 0:
                q.append(x)
            else:
                if len(q) == 0:
                    return False

                y = q.pop(-1)
                if x + y != 0:
                    return False

        return len(q) == 0


# 35. Search Insert Position
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] <= target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1

        return start


# 1480. Running Sum of 1d Array
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        prefix = []
        prefix.append(nums[0])
        for i in range(1, len(nums)):
            new = prefix[i - 1] + nums[i]
            prefix.append(new)

        return prefix


# 1732. Find the Highest Altitude
class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        n = len(gain)
        lst = [0] * (n + 1)
        for i in range(n):
            lst[i + 1] = lst[i] + gain[i]

        return max(lst)


# 2848. Points That Intersect With Cars
class Solution:
    def numberOfPoints(self, nums: list[list[int]]) -> int:
        park = [0] * 102

        for i, j in nums:
            park[i] += 1
            park[j + 1] -= 1

        for i in range(1, len(park)):
            park[i] = park[i] + park[i - 1]

        ans = 0
        for i in park:
            if i != 0:
                ans += 1

        return ans


# 1893. Check if All the Integers in a Range Are Covered
class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        length = len(ranges)
        exist = [0] * 52

        for i in range(length):
            l, r = ranges[i]
            exist[l] += 1
            exist[r + 1] -= 1

        for i in range(1, len(exist)):
            exist[i] = exist[i] + exist[i - 1]

        for i in range(left, right + 1):
            if exist[i] == 0:
                return False

        return True


# 2574. Left and Right Sum Differences
class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        len_n = len(nums)
        left_sum = [0] * len_n
        right_sum = [0] * len_n

        left_sum[0] = 0
        for i in range(1, len_n):
            left_sum[i] = left_sum[i - 1] + nums[i - 1]

        right_sum[len_n - 1] = 0
        for i in range(len_n - 1, 0, -1):
            right_sum[i - 1] = nums[i] + right_sum[i]

        ans = [0] * len_n
        for i in range(len_n):
            ans[i] = abs(left_sum[i] - right_sum[i])

        return ans


# 1991. Find the Middle Index in Array
class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        leng = len(nums)
        prefix = [0] * leng

        prefix[0] = nums[0]
        for i in range(1, leng):
            prefix[i] = prefix[i - 1] + nums[i]

        for i in range(leng):
            left = 0
            right = 0
            if i != 0:
                left = prefix[i - 1]
            if i != leng - 1:
                right = prefix[leng - 1] - prefix[i]

            if left == right:
                return i

        return -1


# 228. Summary Ranges
class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums) <= 1:
            return [str(i) for i in nums]

        leng = len(nums)
        ans = []

        i = 0
        while i < leng:
            l = r = nums[i]
            for j in range(i + 1, leng):
                if r + 1 != nums[j]:
                    break
                r = nums[j]
                i = j

            if l == r:
                ans.append(f"{l}")
            else:
                ans.append(f"{l}->{r}")
            i += 1

        return ans


# 125. Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_lst = []
        for i in s:
            if i in "qwertyuiopasdfghjklzxcvbnm0987654321":
                s_lst.append(i)

        return s_lst == s_lst[::-1]