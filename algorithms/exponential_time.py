""" O(2^n) -> Exponential Time
"""


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    # print(fibonacci(0))
    # print(fibonacci(1))
    # print(fibonacci(2))
    # print(fibonacci(3))
    # print(fibonacci(4))
    # print(fibonacci(5))
    # print(fibonacci(6))
    print(fibonacci(7))
