# EXAMPLE 1:- SORTING OBJECTS WITH NAMED ATTRIBUTE......


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)


emp_1 = Employee('Victor', 30, 90000)
emp_2 = Employee('Melvin', 28, 110000)
emp_3 = Employee('Sarah', 32, 120000)

employees = [emp_1, emp_2, emp_3]


def e_sort(emp):
    return emp.salary


s_employees = sorted(employees, key=e_sort)                 # sorts the salary in ascending order
s_employees = sorted(employees, key=e_sort, reverse=True)   # Sorts salary in descending order
print(s_employees)


# OR use the lambda function to re-write the code in line 20 to 26;
s_employees = sorted(employees, key=lambda e: e.name)            # Sorts result by name
print(s_employees)


# EXAMPLE 2:- Re-writing the above code using the 'key=attrgetter'

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)


from operator import attrgetter               # must include this line of code

emp_1 = Employee('Victor', 30, 90000)
emp_2 = Employee('Melvin', 28, 110000)
emp_3 = Employee('Sarah', 32, 120000)

employees = [emp_1, emp_2, emp_3]


s_employees = sorted(employees, key=attrgetter('age'))

print(s_employees)
