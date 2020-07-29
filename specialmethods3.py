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

# Creating special (Magic-Dunder) methods....;
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.fname, self.lname, self.salary)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

# Summation of the salaries of the 2 employees, we use "__add__"..;
    def __add__(self, other):
        return self.salary + other.salary

# Find the length of characters in employee fullname....
    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Nonso', 'Onyia', 90000)
emp_2 = Employee('Test', 'Python', 100000)


print(emp_1 + emp_2)                                # Prints the result of salary addition....
print(len(emp_1))                                   # O/p character length of employee 1
print(len(emp_2))                                   # O/p character length of employee 2
