def decor(func):
    def inner(string):
        func(string.upper())
    return inner


@decor
def print_text(string):
    print(string + " MAN!")


print_text("What's up,")  # WHAT'S UP, MAN!


def sum_digits(num):
    digits = [int(d) for d in str(num)]
    return sum(digits)


print(sum_digits(5245))
