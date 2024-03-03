# 1 Бинарный поиск | Binary search =====================================================================================
# my_lst = [16, 25, 29, 32, 47, 49, 57, 59, 60, 64, 65, 67, 71, 77, 80, 89, 90, 91, 94]
#
#
# def binary_search(num: int, lst: list):
#     low = 0
#     high = len(lst) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         guess = lst[mid]
#
#         if guess == num:
#             return mid
#         elif guess > num:
#             high = mid - 1
#         else:
#             low = mid + 1
#     else:
#         return None
#
#
# ans = binary_search(1, lst=my_lst)
# print('ans', ans)


