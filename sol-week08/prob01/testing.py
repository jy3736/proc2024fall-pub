import unittest
from main import digits_in_ascending_order
import random
import sys
sys.stdout = sys.stderr

class TestDigitsInAscendingOrder(unittest.TestCase):
    def test_digits_in_ascending_order(self):
        for _ in range(30):
            number = random.randint(100, 999)  # Ensure it's a three-digit number
            digits = [int(d) for d in str(number)]
            expected = "YES" if digits == sorted(digits) else "NO"
            try:
                self.assertEqual(digits_in_ascending_order(number), expected)
            except AssertionError as e:
                print("<<<Failed Test Cases>>>")
                print(f"Input   : {number}")
                print(f"Expected: {expected}\\n")
                print("<<<End of Failed Test Cases>>>")
                raise AssertionError("Some test cases failed")

if __name__ == "__main__":
    unittest.main()

