""" O(n!) -> Factorial

2! = 2 x 1 = 2
3! = 3 x 2 x 1 = 6
4! = 4 x 3 x 2 x 1 = 24
5! = 5 x 4 x 3 x 2 x 1 = 120
6! = 6 x 5 x 4 x 3 x 2 x 1 = 720
7! = 7 x 6 x 5 x 4 x 3 x 2 x 1 = 5.040
8! = 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 40.320
"""


def heap_permutation(data, n):
    if n == 1:
        print(data)
        return

    for i in range(n):
        heap_permutation(data, n-1)
        if n % 2 == 0:
            data[i], data[n-1] = data[n-1], data[i]
        else:
            data[0], data[n-1] = data[n-1], data[0]


if __name__ == "__main__":
    data = [1, 2, 3]
    heap_permutation(data, len(data))
