# EXAMPLE:- Adding a Data science tool the data scientist works with...
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


# Creating a Sub-Class...;
class Data_Scientist(Employee):
    increase_amt = 1.12

    def __init__(self, fname, lname, salary, data_tool):
        super().__init__(fname, lname, salary)              # Handles the '__init__' method in Employee class...
        Employee.__init__(self, fname, lname, salary)            # Means same thing as line 77 (but prefer 77)..
        self.data_tool = data_tool


data_sci_1 = Data_Scientist('Nonso', 'Onyia', 90000, 'Hive')
data_sci_2 = Data_Scientist('Test', 'Python', 100000, 'Spark')


print(data_sci_1.email)
print(data_sci_1.data_tool)
