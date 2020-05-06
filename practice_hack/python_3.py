""" String Formatting."""


def print_formatted(number):
    l1 = len(bin(number)[2:])

    for i in range(1, number + 1):
        print(str(i).rjust(l1, ' '), end=" ")
        print(oct(i)[2:].rjust(l1, ' '), end=" ")
        print(((hex(i)[2:]).upper()).rjust(l1, ' '), end=" ")
        print(bin(i)[2:].rjust(l1, ' '), end=" ")
        print("")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

""" Designer Door Mat."""

# n, m = map(int, input().split())
# pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
# print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))


""" Text Wrap."""

import textwrap


# def wrap(string, max_width):
#     return "\n".join(
#         [string[i:i+max_width] for i in range(0, len(string), max_width)
#          ])
#
#
# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)

""" Text Alignment."""

# #Replace all ______ with rjust, ljust or center.
#
# thickness = int(input()) #This must be an odd number
# c = 'H'
#
# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#
# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#
# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))
#
# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#
# #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

""" String Validators."""

# if __name__ == '__main__':
#     s = input()
#     print(any(c.isalnum() for c in s))
#     print(any(c.isalpha() for c in s))
#     print(any(c.isdigit() for c in s))
#     print(any(c.islower() for c in s))
#     print(any(c.isupper() for c in s))

""" Find a string."""

# def count_substring(string, sub_string):
#     return sum(1 for i in range(len(string)) if sub_string in string[i:i+len(sub_string)])
#
#
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#
#     count = count_substring(string, sub_string)
#     print(count)

""" Mutations."""

# def mutate_string(string, position, character):
#     list2 = list(string)
#     list2[position] = character
#     return ''.join(list2)
#
#
# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)

""" What's Your Name?"""

# def print_full_name(a, b):
#     print(f"Hello {a} {b}! You just delved into python.")
#
#
# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)


""" String Split and Join."""

# def split_and_join(line):
#     return "-".join(line.split())
#
#
# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)


""" sWAP cASE."""

# def swap_case(s):
#     return s.swapcase()
#
#
# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)
