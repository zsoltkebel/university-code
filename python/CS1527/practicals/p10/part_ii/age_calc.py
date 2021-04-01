# Use your knowledge of the GoF design patterns to implement an adapter that allows datetime
# objects to be used with the AgeCalculator class.
#
# disclaimer: base code was provided
# AgeAdapter class is written by me

import datetime


class AgeAdapter:

    def __init__(self, birthday: datetime.date):
        birthday_string = f'{birthday.day}-{birthday.month}-{birthday.year}'
        self._age_calculator = AgeCalculator(birthday_string)

    def calculate_age(self, date: datetime.date):
        date_string = f'{date.day}-{date.month}-{date.year}'
        return self._age_calculator.calculate_age(date_string)


class AgeCalculator:
    """
    Simple class to hold a person's date of birth.
    Doesn't use built-in datetime library, which would have
    been better...
    """
    
    # Initialise the instance using a string date.
    def __init__(self, birthday):
        self.day, self.month, self.year = (
            int(x) for x in birthday.split('-'))

    # Calculate the age (in years) if given another date
    def calculate_age(self, date):
        day, month, year = (int(x) for x in date.split('-'))
        age = year - self.year
        if (month,day) < (self.month,self.day):
            age -= 1
        return age


john = AgeCalculator('13-01-1984')
print(john.calculate_age('1-3-2021'))

john = AgeAdapter(datetime.date(1984, 1, 13))
print(john.calculate_age(datetime.date(2021, 3, 1)))
