from datetime import datetime

class Solution:
    
    def is_weekend(self, date_str):
        date_obj = datetime.strptime(date_str, '%d-%m-%Y')
        return date_obj.strftime('%a')

    def is_leap_year(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def run(self, birthday_date):
        future_dates = []
        birth_date = birthday_date + '-'

        for year in range(2016, 2066):
            if birthday_date == '29-02' and not self.is_leap_year(year):
                continue
            date_str = birth_date + str(year)
            if self.is_weekend(date_str) in ['Fri', 'Sat', 'Sun']:
                future_dates.append(self.is_weekend(date_str)[:3] + '-' + str(year))

        return ' '.join(future_dates)


