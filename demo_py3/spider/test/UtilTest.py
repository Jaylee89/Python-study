import unittest

"""
    reference:
        https://www.cnblogs.com/feng0815/p/8045850.html
        https://www.cnblogs.com/feng0815/p/8045859.html
"""

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)