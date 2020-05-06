""" Triangle Quest 2."""

for i in range(1, int(input())+1):
    print(pow(((pow(10, i)-1)//9), 2))

""" Find Angle MBC."""

# import math

# AB = int(input())
# BC = int(input())

# print(str(int(round(math.degrees(math.atan2(AB, BC)))))+'°')

""" Polar Coordinates."""

# import cmath
#
# print(*cmath.polar(complex(input())), sep='\n')

""" Merge the Tools!"""

# def merge_the_tools(string, k):
#     for i in range(0, len(string), k):
#         s = ""
#         for j in string[i: i + k]:
#             if j not in s:
#                 s += j
#         print(s)
#
#
# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)

""" The Minion Game."""

# v = {"A", "E", "U", "I", "O"}
#
#
# def minion_game(string):
#     l = len(string)
#     k = 0
#     s = 0
#     for i in range(l):
#         if string[i] in v:
#             k += len(range(i, len(string)))
#         elif string[i] not in v:
#             s += len(range(i, len(string)))
#     if s > k:
#         print("Stuart", s)
#     elif s < k:
#         print("Kevin", k)
#     else:
#         print("Draw")
#
#
# if __name__ == '__main__':
#     s = input()
#     minion_game(s)

""" Tuples."""
# if __name__ == '__main__':
#     n = int(input())
#     integer_list = tuple(map(int, input().split(' ')))
#     print(hash(integer_list))


""" Lists."""
# if __name__ == '__main__':
    # N = int(input())
    # list = []
    # for i in range(N):
    #     a = input().split()
    #     if len(a) == 3:
    #         eval("list." + a[0] + "(" + a[1] + "," + a[2] + ")")
    #     elif len(a) == 2:
    #         eval("list." + a[0] + "(" + a[1] + ")")
    #     elif a[0] == "print":
    #         print(list)
    #     else:
    #         eval("list." + a[0] + "()")
