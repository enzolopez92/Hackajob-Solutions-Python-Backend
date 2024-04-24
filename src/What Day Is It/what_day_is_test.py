import unittest
from what_day_is import Solution
class TestSolution(unittest.TestCase):

    def print_test_result(self, input_data, expected_output, actual_output, test_number):
        print(f"Test {test_number}:")
        print(f"Input: {input_data}")
        print(f"Expected Output: {expected_output}")
        print(f"Actual Output: {actual_output}")

    def test_case1(self):
        solution = Solution()
        input_data = "23-10"
        expected_output = "Sun-2016 Fri-2020 Sat-2021 Sun-2022 Fri-2026 Sat-2027 Sat-2032 Sun-2033 Fri-2037 Sat-2038 Sun-2039 Fri-2043 Sun-2044 Fri-2048 Sat-2049 Sun-2050 Fri-2054 Sat-2055 Sat-2060 Sun-2061 Fri-2065"
        actual_output = solution.run(input_data)
        self.print_test_result(input_data, expected_output, actual_output, 1)
        self.assertEqual(actual_output, expected_output)

    def test_case2(self):
        solution = Solution()
        input_data = "29-02"
        expected_output = "Sat-2020 Sun-2032 Fri-2036 Sat-2048 Sun-2060 Fri-2064"
        actual_output = solution.run(input_data)
        self.print_test_result(input_data, expected_output, actual_output, 2)
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()