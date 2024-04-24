import unittest
from string_theory import Solution

class Solution:

    def run(self, p):
        vowels = "aeiou"
        reversed_p = p[::-1]
        reversed_p_with_reversed_cases = ' '.join(word[::-1].swapcase() for word in reversed_p.split())
        p_with_pv = ''.join(['pv' + char if char.lower() in vowels else char for char in p])
        words_in_p = '-'.join(p.split())
        nr_vowels = sum(1 for char in p if char.lower() in vowels)
        nr_consonants = sum(1 for char in p if char.isalpha() and char.lower() not in vowels)

        combined_queries = f"{nr_vowels} {nr_consonants}::{reversed_p_with_reversed_cases}::{words_in_p}::{p_with_pv}"
        return combined_queries


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        p = "ThIs is p"
        expected_output = "2 5::P IS tHiS::ThIs-is-p::ThpvIs pvis p"
        actual_output = self.solution.run(p)
        print("Test 1:")
        print("Input:", p)
        print("Expected Output:", expected_output)
        print("Actual Output:", actual_output)
        self.assertEqual(actual_output, expected_output)

    def test_case_2(self):
        p = "Here is another p"
        expected_output = "6 8::P ANOTHER IS hERE::Here-is-another-p::Hpverpve pvis pvanpvothpver p"
        actual_output = self.solution.run(p)
        print("Test 2:")
        print("Input:", p)
        print("Expected Output:", expected_output)
        print("Actual Output:", actual_output)
        self.assertEqual(actual_output, expected_output)

    def test_case_3(self):
        p = "oaia oie o iii"
        expected_output = "11 0::III O OIE OAIA::oaia-oie-o-iii::pvopvapvipva pvopvipve pvo pvipvipvi"
        actual_output = self.solution.run(p)
        print("Test 3:")
        print("Input:", p)
        print("Expected Output:", expected_output)
        print("Actual Output:", actual_output)
        self.assertEqual(actual_output, expected_output)

    def test_case_4(self):
        p = "The iterator is just clutter"
        expected_output = "9 15::CLUTTER JUST IS ITERATOR tHE::The-iterator-is-just-clutter::Thpve pvitpverpvatpvor pvis jpvust clpvuttpver"
        actual_output = self.solution.run(p)
        print("Test 4:")
        print("Input:", p)
        print("Expected Output:", expected_output)
        print("Actual Output:", actual_output)
        self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    unittest.main()