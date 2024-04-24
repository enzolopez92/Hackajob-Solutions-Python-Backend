import unittest
from roman_numbers import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_lower_bound(self):
        input_n = 1
        expected_output = "I"
        actual_output = self.solution.run(input_n)
        print("\nTest 1:")
        print("Input:", input_n)
        print("Expected Output:", expected_output)
        print("Actual Output:", actual_output)
        self.assertEqual(actual_output, expected_output)

    def test_small_number(self):
        input_n = 9
        expected_output = "IX"
        actual_output = self.solution.run(input_n)
        print("\nTest 2:")
        print("Input:", input_n)
        print("Expected Output:", expected_output)
        print("Actual Output:", actual_output)
        self.assertEqual(actual_output, expected_output)

    def test_round_number(self):
        input_n = 1000
        expected_output = "M"
        actual_output = self.solution.run(input_n)
        print("\nTest 3:")
        print("Input:", input_n)
        print("Expected Output:", expected_output)
        print("Actual Output:", actual_output)
        self.assertEqual(actual_output, expected_output)

    def test_random_number(self):
        input_n = 1994
        expected_output = "MCMXCIV"
        actual_output = self.solution.run(input_n)
        print("\nTest 4:")
        print("Input:", input_n)
        print("Expected Output:", expected_output)
        print("Actual Output:", actual_output)
        self.assertEqual(actual_output, expected_output)

    def test_below_subtraction_point(self):
        input_n = 3999
        expected_output = "MMMCMXCIX"
        actual_output = self.solution.run(input_n)
        print("\nTest 5:")
        print("Input:", input_n)
        print("Expected Output:", expected_output)
        print("Actual Output:", actual_output)
        self.assertEqual(actual_output, expected_output)

    def test_above_subtraction_point(self):
        input_n = 3996
        expected_output = "MMMCMXCVI"
        actual_output = self.solution.run(input_n)
        print("\nTest 6:")
        print("Input:", input_n)
        print("Expected Output:", expected_output)
        print("Actual Output:", actual_output)
        self.assertEqual(actual_output, expected_output)

    def test_upper_bound(self):
        input_n = 9999
        expected_output = "MMMMMMMMMCMXCIX"
        actual_output = self.solution.run(input_n)
        print("\nTest 7:")
        print("Input:", input_n)
        print("Expected Output:", expected_output)
        print("Actual Output:", actual_output)
        self.assertEqual(actual_output, expected_output)

    def test_random_case(self):
        input_n = 4444
        expected_output = "MMMMCDXLIV"
        actual_output = self.solution.run(input_n)
        print("\nTest 8:")
        print("Input:", input_n)
        print("Expected Output:", expected_output)
        print("Actual Output:", actual_output)
        self.assertEqual(actual_output, expected_output)

    def test_power_of_10(self):
        input_n = 5000
        expected_output = "MMMMM"
        actual_output = self.solution.run(input_n)
        print("\nTest 9:")
        print("Input:", input_n)
        print("Expected Output:", expected_output)
        print("Actual Output:", actual_output)
        self.assertEqual(actual_output, expected_output)

    def test_power_of_10_minus_1(self):
        input_n = 9999
        expected_output = "MMMMMMMMMCMXCIX"
        actual_output = self.solution.run(input_n)
        print("\nTest 10:")
        print("Input:", input_n)
        print("Expected Output:", expected_output)
        print("Actual Output:", actual_output)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
