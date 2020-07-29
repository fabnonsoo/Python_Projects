# EXAMPLE:- STATIC METHODS

# Write a simple program/function that will take in a date & return whether or not that's a work day...
import datetime


class Employee:

    num_of_emps = 0
    increase_amt = 1.05

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.email = fname + '.' + lname + '@company.com'

        Employee.num_of_emps += 1

    # fullname and apply_increase method created are known as Regular Methods
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_increase(self):
        self.salary = int(self.salary * self.increase_amt)

# Creating a class method...-> NB: 'cls' in class method is just like 'self' in instance variables
    @classmethod
    def set_increase_amt(cls, amount):
        cls.increase_amt = amount

    @classmethod
    def new_emp(cls, emp_str):
        fname, lname, salary = emp_str.split('-')         # Seperates the emp details w/hyphen
        return cls(fname, lname, salary)                  # Creates a new Employee object

    @staticmethod
    def is_workday(day):
        # In Python, Monday == 0 and Sunday == 6...
        if day.weekday() == 5 or day.weekday() == 6:
            return False                                     # Returns False if it's not a weekday/workday
        return True                                          # Returns True if it's a weekday/workday


emp_1 = Employee('Nonso', 'Onyia', 90000)
emp_2 = Employee('Test', 'Python', 100000)


my_date = datetime.date(2016, 7, 10)                         # Here, 10 July is a Sunday

print(Employee.is_workday(my_date))
