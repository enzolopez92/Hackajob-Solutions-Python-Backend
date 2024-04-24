import unittest
from movie_collection import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        test_number = 1
        n = 3
        m = 3
        movies = [3, 1, 1]
        expected_output = "2,1,0"
        actual_output = self.solution.run(n, m, movies)
        print(f"Test case {test_number}: Input = (n={n}, m={m}, movies={movies}), Expected output = '{expected_output}', Actual output = '{actual_output}'")
        self.assertEqual(actual_output, expected_output)

    def test_case2(self):
        test_number = 2
        n = 5
        m = 3
        movies = [4, 4, 5]
        expected_output = "3,0,4"
        actual_output = self.solution.run(n, m, movies)
        print(f"Test case {test_number}: Input = (n={n}, m={m}, movies={movies}), Expected output = '{expected_output}', Actual output = '{actual_output}'")
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
