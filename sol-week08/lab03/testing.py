import unittest
from main import find_minimum
import random
import sys
sys.stdout = sys.stderr

class TestMinimumOfThree(unittest.TestCase):
    def test_find_minimum(self):
        for _ in range(30):
            a = random.randint(-100, 100)
            b = random.randint(-100, 100)
            c = random.randint(-100, 100)
            expected = min(a, b, c)
            try:
                self.assertEqual(find_minimum(a, b, c), expected)
            except AssertionError as e:
                print("<<<Failed Test Cases>>>")
                print(f"Input   : {a}, {b}, {c}")
                print(f"Expected: {expected}\\n")
                print("<<<End of Failed Test Cases>>>")
                raise AssertionError("Some test cases failed")

if __name__ == "__main__":
    unittest.main()
    