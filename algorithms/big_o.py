""" Factorial — O(n!)."""


def heap_permutation(data, n):
    if n == 1:
        print(data)
        return

    for i in range(n):
        heap_permutation(data, n - 1)
        if n % 2 == 0:
            data[i], data[n - 1] = data[n - 1], data[i]
        else:
            data[0], data[n - 1] = data[n - 1], data[0]


if __name__ == '__main__':
    data = [1, 2, 3, 4]
    heap_permutation(data, len(data))


# """ Exponential Time — O(2^n)."""
#
#
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
#
#
# if __name__ == '__main__':
#     print(fibonacci(3))
#     print(fibonacci(7))


# """ Quadratic Time — O(n²)."""
#
#
# def bubble_sort(data):
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(len(data) - 1):
#             if data[i] > data[i + 1]:
#                 data[i], data[i + 1] = data[i + 1], data[i]
#                 swapped = True
#
#
# if __name__ == '__main__':
#     data = [9, 1, 7, 6, 2, 8, 5, 3, 4, 0]
#     bubble_sort(data)
#     print(data)


# """ Quasilinear Time — O(n log n)."""


# def merge_sort(data):
#     if len(data) <= 1:
#         return
#
#     mid = len(data) // 2
#     left_data = data[:mid]
#     right_data = data[mid:]
#
#     merge_sort(left_data)
#     merge_sort(right_data)
#
#     left_index = 0
#     right_index = 0
#     data_index = 0
#
#     while left_index < len(left_data) and right_index < len(right_data):
#         if left_data[left_index] < right_data[right_index]:
#             data[data_index] = left_data[left_index]
#             left_index += 1
#         else:
#             data[data_index] = right_data[right_index]
#             right_index += 1
#         data_index += 1
#
#     if left_index < len(left_data):
#         del data[data_index:]
#         data += left_data[left_index:]
#     elif right_index < len(right_data):
#         del data[data_index:]
#         data += right_data[right_index:]
#
#
# if __name__ == '__main__':
#     data = [9, 1, 7, 6, 2, 8, 5, 3, 4, 0]
#     merge_sort(data)
#     print(data)

# """ Linear Time — O(n)."""
#
#
# def linear_search(data, value):
#     for index in range(len(data)):
#         if value == data[index]:
#             return index
#     raise ValueError('Value not found in the list')
#
#
# if __name__ == '__main__':
#     data = [1, 2, 9, 8, 3, 4, 7, 6, 5]
#     print(linear_search(data, 7))

# """ Logarithmic Time — O(log n)."""
#
#
# def binary_search(data, value):
#     n = len(data)
#     left = 0
#     right = n - 1
#     while left <= right:
#         middle = (left + right) // 2
#         if value < data[middle]:
#             right = middle - 1
#         elif value > data[middle]:
#             left = middle + 1
#         else:
#             return middle
#     raise ValueError('Value is not in the list')
#
#
# if __name__ == '__main__':
#     data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     print(binary_search(data, 8))


# """ Constant Time — O(1)."""
#
#
# def get_first(data):
#     return data[0]
#
#
# if __name__ == "__main__":
#     data = [1, 2, 9, 5, 3, 4, 8, 6, 7]
#     print(get_first(data))
