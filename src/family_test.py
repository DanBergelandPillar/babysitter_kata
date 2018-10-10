import unittest
import family

class FamilyTest(unittest.TestCase):
    def setUp(self):
        self.fam = family.Family()

    def test(self):
        self.assertIsNotNone(self.fam)

if __name__ == '__main__':
    unittest.main()