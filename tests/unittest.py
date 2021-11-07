import unittest
from ctof import ctof


class CtofTestCase(unittest.TestCase):
    def test_celsius(self):
        result = ctof.cel(89.6)
        self.assertEqual(result, 32)
    def test_celsius_multi(self):
        result1 = ctof.cel([89.6, 91.4])
        result2 = ctof.cel((89.6, 91.4))
        result3 = ctof.cel({89.6, 91.4})
        self.assertEqual(result1, [32, 33])
        self.assertEqual(result2, (32, 33))
        self.assertEqual(result3, {32, 33})
    def test_fahrenheit(self):
        result = ctof.fah(32)
        self.assertEqual(result, 89.6)
    def test_fahrenheit_multi(self):
        result1 = ctof.fah([32, 33])
        result2 = ctof.fah((32, 33))
        result3 = ctof.fah({32, 33})
        self.assertEqual(result1, [89.6, 91.4])
        self.assertEqual(result2, (89.6, 91.4))
        self.assertEqual(result3, {89.6, 91.4})
    def test_invalidparams(self):
        invalidresultc = ctof.cel("invalid")
        invalidresultf = ctof.fah("invalid")
        self.assertEqual(invalidresultc, "Invalid param type")
        self.assertEqual(invalidresultf, "Invalid param type")

if __name__ == '__main__':
    unittest.main()
