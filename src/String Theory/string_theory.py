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

# Test the function
solution = Solution()
p = "The iterator is just clutter"
print(solution.run(p))
