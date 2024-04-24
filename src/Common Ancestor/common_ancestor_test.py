import unittest
from common_ancestor import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        test_number = 1
        index1 = 13
        index2 = 15
        expected_output = 3
        actual_output = self.solution.run(index1, index2)
        print(f"Test case {test_number}: Input = ({index1}, {index2}), Expected output = {expected_output}, Actual output = {actual_output}")
        self.assertEqual(actual_output, expected_output)

    def test_case2(self):
        test_number = 2
        index1 = 11
        index2 = 13
        expected_output = 1
        actual_output = self.solution.run(index1, index2)
        print(f"Test case {test_number}: Input = ({index1}, {index2}), Expected output = {expected_output}, Actual output = {actual_output}")
        self.assertEqual(actual_output, expected_output)

    def test_case3(self):
        test_number = 3
        index1 = 10
        index2 = 11
        expected_output = 5
        actual_output = self.solution.run(index1, index2)
        print(f"Test case {test_number}: Input = ({index1}, {index2}), Expected output = {expected_output}, Actual output = {actual_output}")
        self.assertEqual(actual_output, expected_output)

    def test_case4(self):
        test_number = 4
        index1 = 1
        index2 = 1000000
        expected_output = 1
        actual_output = self.solution.run(index1, index2)
        print(f"Test case {test_number}: Input = ({index1}, {index2}), Expected output = {expected_output}, Actual output = {actual_output}")
        self.assertEqual(actual_output, expected_output)

    def test_case5(self):
        test_number = 5
        index1 = 1000000
        index2 = 1
        expected_output = 1
        actual_output = self.solution.run(index1, index2)
        print(f"Test case {test_number}: Input = ({index1}, {index2}), Expected output = {expected_output}, Actual output = {actual_output}")
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
