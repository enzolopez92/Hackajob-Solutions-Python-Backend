import unittest
from find_singleton import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_student(self):
        # Test case with only one student in the list
        student_list = [5]
        expected_output = 5
        actual_output = self.solution.run(student_list)
        print(f"Test 1 - Input: {student_list}, Expected Output: {expected_output}, Actual Output: {actual_output}")
        self.assertEqual(actual_output, expected_output)

    def test_even_number_of_students(self):
        # Test case with an even number of students
        student_list = [2, 4, 3, 4, 2, 3]
        expected_output = 0
        actual_output = self.solution.run(student_list)
        print(f"Test 2 - Input: {student_list}, Expected Output: {expected_output}, Actual Output: {actual_output}")
        self.assertEqual(actual_output, expected_output)

    def test_odd_number_of_students(self):
        # Test case with an odd number of students
        student_list = [2, 4, 3, 4, 2, 3, 7]
        expected_output = 7
        actual_output = self.solution.run(student_list)
        print(f"Test 3 - Input: {student_list}, Expected Output: {expected_output}, Actual Output: {actual_output}")
        self.assertEqual(actual_output, expected_output)

    def test_negative_student_numbers(self):
        # Test case with negative student numbers
        student_list = [-2, -4, -3, -4, -2, -3, -7]
        expected_output = -7
        actual_output = self.solution.run(student_list)
        print(f"Test 4 - Input: {student_list}, Expected Output: {expected_output}, Actual Output: {actual_output}")
        self.assertEqual(actual_output, expected_output)

    def test_mixed_student_numbers(self):
        # Test case with mixed positive and negative student numbers
        student_list = [2, -4, 3, -4, 2, 3, -7]
        expected_output = -2
        actual_output = self.solution.run(student_list)
        print(f"Test 5 - Input: {student_list}, Expected Output: {expected_output}, Actual Output: {actual_output}")
        self.assertEqual(actual_output, expected_output)

    def test_large_student_numbers(self):
        # Test case with large student numbers
        student_list = [100000, 200000, 300000, 200000, 100000]
        expected_output = 300000
        actual_output = self.solution.run(student_list)
        print(f"Test 6 - Input: {student_list}, Expected Output: {expected_output}, Actual Output: {actual_output}")
        self.assertEqual(actual_output, expected_output)

if __name__ == "__main__":
    unittest.main()
