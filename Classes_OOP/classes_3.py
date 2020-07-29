# EXAMPLE:- Python Object Oriented Programming - CLASS VARIABLES....
class Employee:

# Creating class variables for salary increase/raise....
    increase_amount = 1.05

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.email = fname + '.' + lname + '@company.com'

# Create fullname method;
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

# Create Salary raise/increase method;
    def apply_increase(self):
        self.salary = int(self.salary * self.increase_amount)   # OR '* Employee.increase_amount'


emp_1 = Employee('Nonso', 'Onyia', 90000)
emp_2 = Employee('Test', 'Python', 100000)


print(emp_1.salary)                                # Prints the current salary
emp_1.apply_increase()                             # Invokes the salary increase
print(emp_1.salary)                                # Prints the salary increase

# Prints the salary % increase accessed from the class/'self' instance
print(Employee.increase_amount)
print(emp_1.increase_amount)
print(emp_2.increase_amount)


# Updating our emp_1 salary increase, we set it to-> 1.06....
emp_1.increase_amount = 1.06

print(emp_1.__dict__)

print(Employee.increase_amount)
print(emp_1.increase_amount)
print(emp_2.increase_amount)
