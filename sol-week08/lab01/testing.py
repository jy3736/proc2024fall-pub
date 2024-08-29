import unittest
from main import is_leap_year
import random
import sys
sys.stdout = sys.stderr

class TestLeapYear(unittest.TestCase):
    def test_leap_year(self):
        # Test with 30 random years
        for _ in range(30):
            year = random.randint(1, 9999)
            if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
                expected = "LEAP"
            else:
                expected = "COMMON"
            try:
                self.assertEqual(is_leap_year(year), expected)
            except AssertionError as e:
                print("<<<Failed Test Cases>>>")
                print(f"Input   : {year}")
                print(f"Expected: {expected}\n")
                print("<<<End of Failed Test Cases>>>")
                raise AssertionError("Some test cases failed")

if __name__ == "__main__":
    unittest.main()