import unittest
from main import find_outlier_index
import random
import sys
sys.stdout = sys.stderr

class TestIndexOfOutlier(unittest.TestCase):
    def test_find_outlier_index(self):
        for _ in range(30):
            nums = [random.randint(1, 100)] * 2
            outlier = random.choice([num for num in range(1, 101) if num not in nums])
            nums.insert(random.randint(0, 2), outlier)
            random.shuffle(nums)
            expected = nums.index(outlier) + 1
            try:
                self.assertEqual(find_outlier_index(*nums), expected)
            except AssertionError as e:
                print("<<<Failed Test Cases>>>")
                print(f"Input   : {nums[0]}, {nums[1]}, {nums[2]}")
                print(f"Expected: {expected}\\n")
                print("<<<End of Failed Test Cases>>>")
                raise AssertionError("Some test cases failed")

if __name__ == "__main__":
    unittest.main()
