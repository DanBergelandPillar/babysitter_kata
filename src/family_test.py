import unittest
import family

class FamilyTest(unittest.TestCase):
    def setUp(self):
        self.fam = family.Family()
        self.rate = family.Rate(0,1,15.)

    def test_constructors(self):
        self.assertEqual(self.fam.rates, [])
        self.assertEqual(self.rate.pay_rate, 15.)

if __name__ == '__main__':
    unittest.main()