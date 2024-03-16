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


# 3 Рекурсия | Recursion ===============================================================================================
# def factorial(num):
#     if num == 1:
#         return num
#     else:
#         return num * factorial(num - 1)
#
#
# f5 = factorial(5)
# print(f5)


# 4 Разделяй и властвуй ================================================================================================

# def find_min_square(width, height):
#     '''Функция определяет наименьший размер квадрата'''
#     if height > width:
#         width, height = height, width
#
#     if width % height == 0:
#         return height
#     else:
#         width = width - height * (width // height)
#         return find_min_square(width, height)
#
#
# ans = find_min_square(1680, 640)
# print(ans)

# def find_lst_summ(lst: list):
#     '''Функция находит сумму списка '''
#     if len(lst) == 0:
#         return 0
#     else:
#         return lst[0] + find_lst_summ(lst[1:])
#
#
# my_lst = [1, 2, 3, 4, 5]
# ans = find_lst_summ(my_lst)
# print(ans)

# 4.1 Быстрая сортировка | Quick Sort =================================================================================
# def quicksort(lst: list):
#     if len(lst) < 2:
#         return lst
#     else:
#         pivot = lst.pop(len(lst) // 2)
#         less = [i for i in lst if i <= pivot]
#         grater = [i for i in lst if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(grater)
#
#
# my_lst = [17, 36, 24, 83, 42, 27, 55, 76, 99, 32, 81, 77, 73, 75, 69]
# ans_lst = quicksort(my_lst)
# print(ans_lst)
