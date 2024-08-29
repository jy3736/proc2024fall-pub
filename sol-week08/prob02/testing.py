import unittest
from main import is_palindrome
import random
import sys
sys.stdout = sys.stderr

class TestFourDigitPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        for _ in range(30):
            number = random.randint(1000, 9999)  # Ensure it's a four-digit number
            expected = "YES" if str(number) == str(number)[::-1] else "NO"
            try:
                self.assertEqual(is_palindrome(number), expected)
            except AssertionError as e:
                print("<<<Failed Test Cases>>>")
                print(f"Input   : {number}")
                print(f"Expected: {expected}\\n")
                print("<<<End of Failed Test Cases>>>")
                raise AssertionError("Some test cases failed")

if __name__ == "__main__":
    unittest.main()