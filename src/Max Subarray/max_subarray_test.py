import unittest
from max_subarray import Solution

class TestMaximumSubarray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        # Example input and output
        input_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected_output = 6
        actual_output = self.solution.run(input_array)
        print(f"Test 1 - Input: {input_array}, Expected Output: {expected_output}, Actual Output: {actual_output}")
        self.assertEqual(actual_output, expected_output)

    def test_single_element(self):
        # Test case with a single element in the array
        input_array = [5]
        expected_output = 5
        actual_output = self.solution.run(input_array)
        print(f"Test 2 - Input: {input_array}, Expected Output: {expected_output}, Actual Output: {actual_output}")
        self.assertEqual(actual_output, expected_output)

    def test_all_negative(self):
        # Test case with all negative numbers
        input_array = [-5, -3, -9, -1, -7]
        expected_output = -1
        actual_output = self.solution.run(input_array)
        print(f"Test 3 - Input: {input_array}, Expected Output: {expected_output}, Actual Output: {actual_output}")
        self.assertEqual(actual_output, expected_output)

    def test_all_positive(self):
        # Test case with all positive numbers
        input_array = [2, 4, 6, 1, 8]
        expected_output = 21
        actual_output = self.solution.run(input_array)
        print(f"Test 4 - Input: {input_array}, Expected Output: {expected_output}, Actual Output: {actual_output}")
        self.assertEqual(actual_output, expected_output)

    def test_mixed_numbers(self):
        # Test case with mixed positive and negative numbers
        input_array = [-2, 3, -1, 4, -2, 1, 5, -3]
        expected_output = 10
        actual_output = self.solution.run(input_array)
        print(f"Test 5 - Input: {input_array}, Expected Output: {expected_output}, Actual Output: {actual_output}")
        self.assertEqual(actual_output, expected_output)

if __name__ == "__main__":
    unittest.main()
