import unittest
import calculator
import constants

class CalculatorTest(unittest.TestCase):
    def test_FamilyAPays15perHourFrom5pmTo11pm(self):
        wage = calculator.calculate('5pm','11pm',constants.FAMILY_A)
        self.assertEqual(wage, 6*15.)

    def test_FamilyAPays20perHourFrom11pmTo4am(self):
        wage = calculator.calculate('11pm','4am',constants.FAMILY_A)
        self.assertEqual(wage, 5*20.)

    def test_FamilyABillsProperlyForFullNight(self):
        wage = calculator.calculate('5pm','4am',constants.FAMILY_A)
        self.assertEqual(wage, 5*20. + 6*15.)
    
    def test_FamilyAPaysPartialShift(self):
        wage = calculator.calculate('5pm','6pm',constants.FAMILY_A)
        self.assertEqual(wage, 1*15.)

    def test_FamilyAPaysShiftOverlap(self):
        wage = calculator.calculate('10pm','12pm',constants.FAMILY_A)
        self.assertEqual(wage, 1*15. + 1*20.)        

if __name__ == '__main__':
    unittest.main()