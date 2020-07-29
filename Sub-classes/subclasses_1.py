# Python OOP - INHERITANCE - CREATING SUB-CLASSES...

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


class Data_Scientist(Employee):
    increase_amt = 1.12


data_sci_1 = Employee('Nonso', 'Onyia', 90000)           # This can be changed to Data_Scientist as in line 29
data_sci_2 = Data_Scientist('Test', 'Python', 100000)


print(help(Data_Scientist))            # Helps reveal how/what Data_Scientist inherited from Employee

print(data_sci_2.email)

# Nothing changes because of Employee() in line 28
print(data_sci_1.salary)
data_sci_1.apply_increase()
print(data_sci_1.salary)

# Changes was implemented because of Data_Scientist() in line 29
print(data_sci_2.salary)
data_sci_2.apply_increase()
print(data_sci_2.salary)
