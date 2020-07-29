class Employee:
    pass


emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

# Creating INSTANCE variable for each Employee class....;
emp_1.firstname = 'Nonso'
emp_1.lastname = 'Onyia'
emp_1.email = 'nonyia@company.com'
emp_1.salary = 90000

emp_2.firstname = 'Tana'
emp_2.lastname = 'Ekeke'
emp_2.email = 'tekeke@company.com'
emp_2.salary = 100000


print(emp_1.email)
print(emp_2.email)
