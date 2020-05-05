""" Iterables and Iterators."""

from itertools import combinations

N = int(input())
L = input().split()
K = int(input())

C = list(combinations(L, K))
F = filter(lambda c: 'a' in c, C)

print("{0:.3}".format(len(list(F))/len(C)))

""" Compress the String!"""

# from itertools import groupby
# print(*[(len(list(c)), int(k)) for k, c in groupby(input())])

""" itertools.combinations_with_replacement()."""

# if __name__ == '__main__':
#     from itertools import combinations_with_replacement
#
#     lis = input().split(' ')
#
#     for i in combinations_with_replacement(sorted(lis[0]), int(lis[1])):
#         print(''.join(i))


""" Finding the percentage."""
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#
#     print("%.2f" % (sum(student_marks[query_name]) / len(student_marks[query_name])))

# if __name__ == '__main__':
#     mark_sheet = []
#     score_list = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         mark_sheet += [[name, score]]
#         score_list += [score]
#
#     score_list = list(dict.fromkeys(score_list))
#     b = sorted(score_list)[1]
#
#     for a, c in sorted(mark_sheet):
#         if c == b:
#             print(a)

# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#
#     arr_set = set(arr)
#     arr_list = list(arr_set)
#     arr_list.sort(reverse=True)
#     print(arr_list[1])

# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#
#     print([[i, j, f] for i in range(x + 1) for j in range(y + 1)
#            for f in range(z + 1) if i + j + f != n])

# if __name__ == '__main__':
#     integers_ = input().split()
#     integers_ = map(int, integers_)
#     n = map(int, input().split())
#     A = set(map(int, input().split()))
#     B = set(map(int, input().split()))
#
#     counter = 0
#     for i in n:
#         if i in A:
#             counter += 1
#         elif i in B:
#             counter -= 1
#
#     print(counter)

# if __name__ == '__main__':
#
#     numbers1 = int(input())
#     set1 = set(map(int, input().split()))
#     numbers2 = int(input())
#     set2 = set(map(int, input().split()))
#     set3 = (set1.difference(set2)).union(set2.difference(set1))
#
#     for i in sorted(list(set3)):
#         print(i)

# if __name__ == '__main__':
#     n = int(input())
#     for i in range(n):
#         print(i + 1, end="")

# def is_leap(year):
#     leap = False
#
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 leap = True
#             else:
#                 leap = False
#         else:
#             leap = True
#     else:
#         leap = False
#
#     return leap
#
#
# year = int(input())
# print(is_leap(year))
# if __name__ == '__main__':
#     n = int(input())
#     for i in range(n):
#         print(i*i)

# import math
# import os
# import random
# import re
# import sys
#
#
# if __name__ == '__main__':
#     n = int(input().strip())
#     if n % 2 == 0 and n in range(2, 6):
#         print("Not Weird")
#     elif n % 2 == 0 and n in range(6, 21):
#         print("Weird")
#     elif n % 2 == 0 and n > 20:
#         print("Not Weird")
#     else:
#         print("Weird")

