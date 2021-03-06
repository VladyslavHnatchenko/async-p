import unittest


class MyClass(object):
    def __init__(self, foo):
        if foo != 1:
            raise ValueError("foo is not equal to 1!")


class MyClass2(object):
    def __init__(self):
        pass


class TestFoo(unittest.TestCase):
    def test_insufficient_args(self):
        foo = 0
        self.assertRaises(ValueError, MyClass, foo)

    def test_args(self):
        self.assertRaises(TypeError, MyClass2, ("fsa", "fds"))


if __name__ == "__main__":
    unittest.main()
