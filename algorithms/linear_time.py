""" O(n) -> Linear Time

for value in data:
    print(value)
"""


def max_elem(data):
    max_item = data[0]

    for item in data:
        if item > max_item:
            max_item = item
    return max_item


if __name__ == "__main__":
    data = [2, 16, 7, 9, 87, 23, 12]
    print(max_elem(data))

# def linear_search(data, value):
#     for index in range(len(data)):
#         if value == data[index]:
#             return index
#     raise ValueError("Value not found in the list")
#
#
# if __name__ == "__main__":
#     data = [1, 2, 9, 8, 3, 4, 7, 6, 5]
#     print(linear_search(data, 7))
