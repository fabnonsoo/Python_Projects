# Without creating the def email(self) method, the updated email values in our class won't change
# Even if every other thing (fname) changes...
# fullname will definitely be updated because we've set the def fullname(self) method...


class Employee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.fname, self.lname)

    @property
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)


emp_1 = Employee('George', 'McKinsey')

emp_1.fname = 'Abigail'

print(emp_1.fname)
print(emp_1.fullname)               # Prints w/@property (must add @property on top def fullname method)
print(emp_1.email)                  # Prints w/@property ((must add @property on top of def email method))
