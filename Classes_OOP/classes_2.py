# EXAMPLE 1i:- Automatically creating instances for each Employee class using '__init__' method
class Employee:

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.email = fname + '.' + lname + '@company.com'


emp_1 = Employee('Nonso', 'Onyia', 90000)
emp_2 = Employee('Test', 'Python', 100000)

print(emp_1.email)
print(emp_2.email)

print('{} {}'.format(emp_1.fname, emp_1.lname))             # O/P the full name of an Employee...


# EXAMPLE 1ii:- Re-writing the Employee class to O/p the fullname...
class Employee:

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.email = fname + '.' + lname + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)


emp_1 = Employee('Nonso', 'Onyia', 90000)
emp_2 = Employee('Test', 'Python', 100000)

print(emp_1.fullname())
print(emp_2.fullname())

print(Employee.fullname(emp_1))
print(emp_2.salary)
