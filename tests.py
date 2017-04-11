import unittest
from format_price import format_price


class TestFormatPrice(unittest.TestCase):

    def test_format_price(self):
        self.assertEqual(format_price('3242.999999'), '3 243')
        self.assertEqual(format_price('0'), '0')
        self.assertEqual(format_price('-543433.52355'), '0')
        self.assertEqual(format_price('432424234242'), '432 424 234 242')

    def test_comma_instead_of_dot(self):
        self.assertEqual(format_price('980,22'), '980')

    def test_valueError(self):
        self.assertEqual(format_price('price: 12312.3242'), '0')

    def test_typeError(self):
        self.assertEqual(format_price(None), '0')

if __name__ == '__main__':
    unittest.main()