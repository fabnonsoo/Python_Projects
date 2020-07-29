# EXAMPLE:- Creating a Class Variable to find the number of employees in the company

class Employee:

    # Creating class variables
    num_of_emps = 0
    increase_amount = 1.05

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.email = fname + '.' + lname + '@company.com'

        Employee.num_of_emps += 1

# Create fullname method;
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

# Create Salary raise/increase method;
    def apply_increase(self):
        self.salary = int(self.salary * self.increase_amount)


emp_1 = Employee('Nonso', 'Onyia', 90000)
emp_2 = Employee('Test', 'Python', 100000)

print(Employee.num_of_emps)
