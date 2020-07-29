# Python OOP - CLASS METHODS.....

# EXAMPLE:- Creating a class method that increses the salary of Employees
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

# Creating a class method...-> 'cls' in class method is just like 'self' in instance variables
    @classmethod
    def set_increase_amt(cls, amount):
        cls.increase_amt = amount


emp_1 = Employee('Nonso', 'Onyia', 90000)
emp_2 = Employee('Test', 'Python', 100000)

Employee.set_increase_amt(1.06)

print(Employee.increase_amt)
print(emp_1.increase_amt)
print(emp_2.increase_amt)
