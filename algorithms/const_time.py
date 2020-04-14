""" O(1) -> Constant Time

if a > b:
    return True
else:
    return False
"""


def odd_or_even(n):
    if n % 2 == 0:
        print("Even")
    if n % 2 != 0:
        print("Odd")


if __name__ == "__main__":
    odd_or_even(2)
    odd_or_even(3)

# def get_first(data):
#     return data[0]
#
#
# if __name__ == "__main__":
#     data = [1, 2, 9, 8, 3, 4, 7, 5, 6]
#     print(get_first(data))
