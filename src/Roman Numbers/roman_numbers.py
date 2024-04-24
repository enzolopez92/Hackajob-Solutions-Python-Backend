class Solution:
    def int_to_roman(self, n):
        # Define a mapping of Roman numerals to their corresponding integer values
        roman_numerals = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
            100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
            10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }

        # Initialize an empty string to store the Roman numeral representation
        roman_numeral = ''

        # Iterate through the mapping in descending order of values
        for value, numeral in sorted(roman_numerals.items(), reverse=True):
            # Subtract the largest possible Roman numeral value from n
            while n >= value:
                n -= value
                # Append the corresponding Roman numeral to the result string
                roman_numeral += numeral

        return roman_numeral

    def run(self, n):
        # Convert the given integer 'n' into a Roman numeral string
        n_in_roman_alphabet = self.int_to_roman(n)
        return n_in_roman_alphabet