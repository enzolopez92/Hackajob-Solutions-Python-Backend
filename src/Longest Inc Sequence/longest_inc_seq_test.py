import unittest
from longest_inc_seq import Solution
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        seq = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
        expected = 6
        result = self.solution.run(seq)
        print(f"Test 1:")
        print("Input:", seq)
        print("Expected Output:", expected)
        print("Actual Output:", result)
        self.assertEqual(result, expected)

    def test_case_2(self):
        seq = [5, 2, 8, 6, 3, 6, 9, 7]
        expected = 4
        result = self.solution.run(seq)
        print(f"Test 2:")
        print("Input:", seq)
        print("Expected Output:", expected)
        print("Actual Output:", result)
        self.assertEqual(result, expected)

    def test_case_3(self):
        seq = [1, 2, 3, 4, 5]
        expected = 5
        result = self.solution.run(seq)
        print(f"Test 3:")
        print("Input:", seq)
        print("Expected Output:", expected)
        print("Actual Output:", result)
        self.assertEqual(result, expected)

    def test_case_4(self):
        seq = [5, 4, 3, 2, 1]
        expected = 1
        result = self.solution.run(seq)
        print(f"Test 4:")
        print("Input:", seq)
        print("Expected Output:", expected)
        print("Actual Output:", result)
        self.assertEqual(result, expected)



    def test_case_5(self):
        seq = [1]
        expected = 1
        result = self.solution.run(seq)
        print(f"Test 5:")
        print("Input:", seq)
        print("Expected Output:", expected)
        print("Actual Output:", result)
        self.assertEqual(result, expected)

    def test_case_6(self):
        seq = [1, 1, 1, 1, 1]
        expected = 1
        result = self.solution.run(seq)
        print(f"Test 6:")
        print("Input:", seq)
        print("Expected Output:", expected)
        print("Actual Output:", result)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()