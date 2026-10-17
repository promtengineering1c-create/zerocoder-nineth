import unittest

from AT01.main import divide


class TestMath(unittest.TestCase):    
    def test_divide(self):
        self.assertEqual(divide(12,5), 2)
        self.assertEqual(divide(12,5), 2)
        self.assertRaises(ValueError, divide, 6, 0)


if __name__ == '__main__':
    unittest.main()