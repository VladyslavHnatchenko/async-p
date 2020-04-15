def file_ext(data):
    name = data.split(".")[0]
    ext = data.split(".")[1]
    try:
        if len(ext) <= 1:
            print(f"We don't have expansion for file {name} ...")
        elif len(ext) >= 2:
            print(f"File {name} has expansion: {ext} ...")
    except IndexError:
        print("Without expansion")
    else:
        print("Without expansion")


file_ext("python.py")
file_ext("python.p")
file_ext("python")
file_ext("python.java")
file_ext("")

# def pascal_triangle(n):
#     row = [1]
#     y = [0]
#     for x in range(max(n, 0)):
#         print(row)
#         row = [left + right for left, right in zip(row+y, y+row)]
#
#
# pascal_triangle(6)

# def min_max(data):
#     min_ = data[0]
#     max_ = data[-1]
#
#     for x in data:
#         if x < min_:
#             min_ = x
#         if x > max_:
#             max_ = x
#     return f"MIN: {min_}, MAX: {max_}"
#
#
# a = [2, 3, 4, 5, 10, 11, 1]
# b = [333, 4, 3, 222, 12, 3, 12313]
#
# print(min_max(a))
# print(min_max(b))
