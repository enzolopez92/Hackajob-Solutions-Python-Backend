# Solution Explanation: 

1. int_to_roman method:
- This method takes an integer n as input and converts it into a Roman numeral string.
- It defines a mapping of Roman numerals to their corresponding integer values in a dictionary called roman_numerals.
- The keys of the dictionary represent the integer values, and the values represent the corresponding Roman numeral symbols.
- It initializes an empty string roman_numeral to store the Roman numeral representation of n.
- It iterates through the roman_numerals dictionary in descending order of values using sorted(roman_numerals.items(), reverse=True).
- Inside the loop, it subtracts the largest possible Roman numeral value from n as many times as possible while n is greater than or equal to the current value.
- For each subtraction, it appends the corresponding Roman numeral symbol to the roman_numeral string.
- Finally, it returns the roman_numeral string representing the Roman numeral equivalent of the input integer n.

2. run method:
- This method serves as an interface to convert an integer n into its Roman numeral representation.
- It calls the int_to_roman method with the input integer n to get the Roman numeral string representation.
- It returns the resulting Roman numeral string.