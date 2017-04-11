import unittest
from format_price import format_price


class TestFormatPrice(unittest.TestCase):

    def test_price_with_dot(self):
        self.assertEqual(format_price('3242.999999'), '3 243')
        self.assertEqual(format_price('432424234242'), '432 424 234 242')
        self.assertEqual(format_price('0'), '0')
        self.assertEqual(format_price('-543433.52355'), '0')

    def test_price_with_comma(self):
        self.assertEqual(format_price('980,22'), '980')
        self.assertEqual(format_price('5235523,930055'), '5 235 524')
        self.assertEqual(format_price('0,00000'), '0')
        self.assertEqual(format_price('-43283,000000'), '0')

    def test_valueError(self):
        self.assertEqual(format_price('price: 12312.3242'), '0')

    def test_typeError(self):
        self.assertEqual(format_price(None), '0')

if __name__ == '__main__':
    unittest.main()
