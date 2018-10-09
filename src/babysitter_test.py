import unittest
import babysitter


class BabysitterTest(unittest.TestCase):
    def setUp(self):
        self.bs_under_test = babysitter.babysitter()
    
    def test_exists(self):
        self.assertEqual(self.bs_under_test.getTimeSpan(), 11)

if __name__ == '__main__':
    unittest.main()