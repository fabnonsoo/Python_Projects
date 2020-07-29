# KEYWORD AND POSITIONAL ARGUMENTS IN PYTHON.....


# EXAMPLE 1:-

def intrinx(name="Epa", action="drove", location="to Lekki"):
    print(name, action, location)


intrinx()
intrinx("Bertrand", "plays golf", "in the USA")
intrinx(action="moved")
intrinx(action="is from", location="Ngwo, Enugu State")


# EXAMPLE 2:- args & kwargs allows us to accept an arbitrary number of positional or keyword arguments

def student_data(*args, **kwargs):
    print(args)
    print(kwargs)


student_data('Robotics', 'IOT', 'Math', name='Cindy', city='Seattle', age=24)


# EXAMPLE 3:-

def addNums(*args):
    total = 0
    for c in args:
        total += c
    print(total)


addNums(56)
addNums(45, 23, 89, 7)


# EXAMPLE 4:-

def student_data(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ['Robotics', 'IOT', 'Math']
data = {'name': 'Cindy', 'city': 'Seattle', 'age': 24}

student_data(*courses, **data)
