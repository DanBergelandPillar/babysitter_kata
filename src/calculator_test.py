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

    def test_FamilyBPays12perHourBefore10pm(self):
        wage = calculator.calculate('5pm','10pm',constants.FAMILY_B)
        self.assertEqual(wage, 5*12.) 

    def test_FamilyBPays8PerHour10pmtoMidnight(self):
        wage = calculator.calculate('10pm','12pm',constants.FAMILY_B)
        self.assertEqual(wage, 2*8.)   

    def test_FamilyBPays16AfterMidnight(self):
        wage = calculator.calculate('12pm','4am',constants.FAMILY_B)
        self.assertEqual(wage, 4*16.)       

    def test_FamilyBFullNightPay(self):
        wage = calculator.calculate('5pm','4am',constants.FAMILY_B)
        self.assertEqual(wage, 5*12 + 2*8 + 4*16)

    def test_FamilyBPartialShiftsHasCorrectPay(self):
        wage = calculator.calculate('9pm','1am',constants.FAMILY_B)
        self.assertEqual(wage, 1*12 + 2*8 + 1*16)

    def test_FamilyCPays21Before9pm(self):
        wage = calculator.calculate('5pm','9pm',constants.FAMILY_C)
        self.assertEqual(wage, 4*21)

    def test_FamilyCPays15After9pm(self):
        wage = calculator.calculate('9pm','4am',constants.FAMILY_C)
        self.assertEqual(wage, 7*15)

if __name__ == '__main__':
    unittest.main()