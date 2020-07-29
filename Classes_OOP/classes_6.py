# EXAMPLE:- Creating a class method that adds new Employees to the company
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


emp_1 = Employee('Nonso', 'Onyia', 90000)
emp_2 = Employee('Test', 'Python', 100000)


emp_str_1 = 'Victor-Chinelo-70000'
emp_str_2 = 'Sarah-Mckinsey-80000'
emp_str_3 = 'Tana-Ekeke-85000'


# new_emp_1 or 2 or 3 must be defined, else there'll be no printed o/p: gives an Error
new_emp_1 = Employee.new_emp(emp_str_1)
new_emp_2 = Employee.new_emp(emp_str_2)
new_emp_3 = Employee.new_emp(emp_str_3)

print(Employee.num_of_emps)                       # Prints total number of employees

print(new_emp_1.salary)
print(new_emp_2.lname)
print(new_emp_3.email)
