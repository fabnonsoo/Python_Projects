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

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.fname, self.lname, self.salary)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)


emp_1 = Employee('Nonso', 'Onyia', 90000)
emp_2 = Employee('Test', 'Python', 100000)

print(emp_1)
print(emp_2)

print(repr(emp_2))
print(str(emp_1))

print(emp_1.__repr__())
print(emp_2.__str__())
