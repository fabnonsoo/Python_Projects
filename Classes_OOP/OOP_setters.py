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

# Creating a Setter for the attribute.....
    @fullname.setter
    def fullname(self, name):
        fname, lname = name.split(' ')
        self.fname = fname
        self.lname = lname


emp_1 = Employee('Abigail', 'Ude')
emp_1.fullname = 'Chinelo Onyia'

print(emp_1.fname)
print(emp_1.email)
print(emp_1.fullname)
