import unittest
import ctof


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
    def test_kelvin(self):
        result1 = ctof.kel(0, "C")
        result2 = ctof.kel(32, "F")
        self.assertEqual(result1, 273.15)
        self.assertEqual(result2, 273.15)
    def test_kelvin_multi(self):
        result1 = ctof.kel([0, 100, 200], "C")
        result2 = ctof.kel((0, 100, 200), "C")
        result3 = ctof.kel({0, 100, 200}, "C")
        result4 = ctof.kel([32, 212, 392], "F")
        result5 = ctof.kel((32, 212, 392), "F")
        result6 = ctof.kel({32, 212, 392}, "F")
        self.assertEqual(result1, [273.15, 373.15, 473.15])
        self.assertEqual(result2, (273.15, 373.15, 473.15))
        self.assertEqual(result3, {273.15, 373.15, 473.15})
        self.assertEqual(result4, [273.15, 373.15, 473.15])
        self.assertEqual(result5, (273.15, 373.15, 473.15))
        self.assertEqual(result6, {273.15, 373.15, 473.15})
    def test_invalidparams(self):
        invalidresultc = ctof.cel("invalid")
        invalidresultf = ctof.fah("invalid")
        self.assertEqual(invalidresultc, "Invalid param type")
        self.assertEqual(invalidresultf, "Invalid param type")



if __name__ == '__main__':
    unittest.main()
