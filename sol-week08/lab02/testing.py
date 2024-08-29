import unittest
from main import can_split_chocolate
import random
import sys
sys.stdout = sys.stderr

class TestChocolateSplit(unittest.TestCase):
    def test_can_split_chocolate(self):
        for _ in range(30):
            n = random.randint(1, 50)
            m = random.randint(1, 50)
            k = random.randint(1, n*m)
            expected = "YES" if (k < n * m) and ((k % n == 0) or (k % m == 0)) else "NO"
            try:
                self.assertEqual(can_split_chocolate(n, m, k), expected)
            except AssertionError as e:
                print("<<<Failed Test Cases>>>")
                print(f"Input   : {n}, {m}, {k}")
                print(f"Expected: {expected}\\n")
                print("<<<End of Failed Test Cases>>>")
                raise AssertionError("Some test cases failed")

if __name__ == "__main__":
    unittest.main()
    