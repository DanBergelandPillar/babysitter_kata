import unittest
import calculator
import constants

class CalculatorTest(unittest.TestCase):

    def test_RateConstructor(self):
        rate = calculator.Rate(0,1,15.)
        self.assertEqual(rate.pay_rate, 15.)
        self.assertEqual(rate.start_int, 0)
        self.assertEqual(rate.stop_int, 1)

    def test_FamilyAPays15perHourFrom5pmTo11pm(self):
        wage = calculator.calculate('5pm','11pm',constants.FAMILY_A)
        self.assertEqual(wage, 6*15.)

if __name__ == '__main__':
    unittest.main()