# binary_search (Бинарный поиск). Только для отсортированных массивов. O(log n)
def binary_search(arr_b, x):
  low = 0
  high = len(arr_b) - 1
  while low <= high:
    mid = (low + high) // 2
    if arr_b[mid] == x:
      return mid
    elif arr_b[mid] < x:
      low = mid + 1
    else:
      high = mid - 1
  return -1
arr_b = [1, 2, 3, 4, 5, 6, 10]
x = 5
res = binary_search(arr_b, x)
"""if res != -1:
  print(f"Элемент найден. Индекс: {res}")
else:
  print("Элемент не найден")"""

# selection_sort (Сортировка выбором). O(n^2)
def selection_sort(arr_s):
  for i in range(len(arr_s)):
    min_idx = i
    for j in range(i + 1, len(arr_s)):
      if arr_s[j] < arr_s[min_idx]:
        min_idx = j
    arr_s[i], arr_s[min_idx] = arr_s[min_idx], arr_s[i]
with open('float_1745761406157.txt', 'r') as f:
  arr_s = [float(num) for num in f.read().split()]
selection_sort(arr_s)
#print(arr_s)

# insertion_sort (Сортировка вставками). O(n^2)
def insertion_sort(arr_i):
  for i in range(1, len(arr_i)):
    key = arr_i[i]
    j = i - 1
    while j >= 0 and arr_i[j] > key:
      arr_i[j + 1] = arr_i[j]
      j -= 1
    arr_i[j + 1] = key
with open('float_1745761406157.txt', 'r') as f:
  arr_i = [float(num) for num in f.read().split()]
insertion_sort(arr_i)
#print(arr_i)

# quick_sort (Быстрая сортировка). O(n log n)
def quicksort(arr, low, high):
  if low >= high:
    return
  pivot = arr[high]
  i = low
  for j in range(low, high):
      if arr[j] <= pivot:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
  arr[i], arr[high] = arr[high], arr[i]
  quicksort(arr, low, i - 1)
  quicksort(arr, i + 1, high)
with open('float_1745761406157.txt', 'r') as f:
  arr = [float(num) for num in f.read().split()]
quicksort(arr, 0, len(arr) - 1)
#print(arr)

# merge_sort (Сортировка слиянием). O(n log n)
def merge_sort(arr_m):
  if len(arr_m) <= 1:
    return arr_m
  mid = len(arr_m) // 2
  left_half = arr_m[:mid]
  right_half = arr_m[mid:]
  left_half = merge_sort(left_half)
  right_half = merge_sort(right_half)
  return merge(left_half, right_half)
def merge(left, right):
  sorted_arr_m = []
  i = j = 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      sorted_arr_m.append(left[i])
      i += 1
    else:
      sorted_arr_m.append(right[j])
      j += 1
  sorted_arr_m.extend(left[i:])
  sorted_arr_m.extend(right[j:])
  return sorted_arr_m
with open('float_1745761406157.txt', 'r') as f:
  arr_m = [float(num) for num in f.read().split()]
sorted_arr_m = merge_sort(arr_m)
#print(sorted_arr_m)
