import unittest
import babysitter
import datetime

class BabysitterTest(unittest.TestCase):
    def setUp(self):
        self.bs_under_test = babysitter.babysitter()
    
    def test_set_start_time_sets_time(self):
        self.bs_under_test.set_start_time('8pm')
        self.assertEqual(self.bs_under_test.start_time_int, 3)

    def test_startTimeBefore5pmCoercedTo5pmIfInvalid(self):
        self.bs_under_test.set_start_time('4pm')
        self.assertEqual(self.bs_under_test.start_time_int, 0)

    def test_set_end_time_sets_time(self):
        self.bs_under_test.set_end_time('12pm')
        self.assertEqual(self.bs_under_test.end_time_int, 7)

    def test_set_end_timeCoercedTo4amIfInvalid(self):
        self.bs_under_test.set_end_time('5am')
        self.assertEqual(self.bs_under_test.end_time_int, 11)

    def test_babySitterConstructor(self):
        test_babysitter = babysitter.babysitter('10pm', '12pm')
        self.assertEqual(test_babysitter.start_time_int, 5)


if __name__ == '__main__':
    unittest.main()