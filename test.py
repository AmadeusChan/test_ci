import unittest

class MyTestCase(unittest.TestCase):
    def test1(self):
        a = 1
        b = 2
        assert(a + b == 3)

    def test2(self):
        x = 1
        y = 2
        assert(x * y == 2)

unittest.main()
