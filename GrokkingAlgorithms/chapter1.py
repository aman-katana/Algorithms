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

# 2 Сортировка выбором | Selection Sort ================================================================================
# my_lst = [16, 25, 32, 47, 57, 60, 65, 71, 80, 94]
#
#
# def find_smallest(lst) -> int | None:
#     '''Returns index of smallest obj if exists'''
#     if len(lst) < 1:
#         return None
#     smallest = lst[0]
#     smallest_index = 0
#     for i in range(len(lst)):
#         if lst[i] < smallest:
#             smallest = lst[i]
#             smallest_index = i
#     return smallest_index
#
#
# def selectionSort(lst: list):
#     new_lst = []
#     for i in range(len(lst)):
#         smallest_index = find_smallest(lst)
#         new_lst.append(lst.pop(smallest_index))
#     return new_lst
#
#
# print(selectionSort(my_lst))

