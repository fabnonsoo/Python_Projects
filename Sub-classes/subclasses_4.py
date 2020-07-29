# EXAMPLE:- USING 'isinstance' and 'issubclass' in PYTHON...
# 'isinstance' tells us if an object is an instance of a class...
# 'issubclass' tells us if a class is a sub-class of another...


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
        super().__init__(fname, lname, salary)
        self.data_tool = data_tool


class Manager(Employee):

    def __init__(self, fname, lname, salary, employees=None):
        super().__init__(fname, lname, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

# Adds employees to the Manager's list...
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

# Removes employees off the Manager's list...
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

# Prints employees from the Manager's list...
    def print_emps(self):
        for emp in self.employees:
            print('Employee Name -->', emp.fullname())


data_sci_1 = Data_Scientist('Nonso', 'Onyia', 90000, 'Hive')
data_sci_2 = Data_Scientist('Test', 'Python', 100000, 'Spark')

mgr_1 = Manager('Tana', 'Ekeke', 130000, [data_sci_2])


# print(isinstance(mgr_1, Manager))                 # means is mgr_1 an instance of sub-class Manager?
# print(isinstance(mgr_1, Employee))                # means is mgr_1 an instance of class Employee?
print(isinstance(mgr_1, Data_Scientist))
print(isinstance(data_sci_2, Data_Scientist))


print(issubclass(Manager, Employee))
print(issubclass(Manager, Data_Scientist))
