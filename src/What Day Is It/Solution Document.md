# Solution Documentation

### Solution Class: 
This class contains the implementation of the main logic for solving the problem. It has two methods:

- is_weekend(date_str): This method takes a date string in the format '%d-%m-%Y' (e.g., '23-10-2023') as input and returns the abbreviated day of the week (e.g., 'Sun', 'Mon', etc.).

- is_leap_year(year): This method checks if a given year is a leap year and returns True or False accordingly.
run(birthday_date): This method takes the birthday date string in the format 'dd-mm' as input and calculates the future dates where the birthday falls on a Friday, Saturday, or Sunday, starting from 2016 up to 2065. It returns a string containing these future dates in the format "wday-yyyy", separated by spaces.