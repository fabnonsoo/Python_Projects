# FUNCTIONS IN PYTHON:- Keeping your code 'DRY' in programming means don't repeat yourself when coding, use a function!

# EXAMPLE 1:-


def hello_func():
    print('My First Function.')


hello_func()
hello_func()


# EXAMPLE 2:-

def hello_func():
    return 'Hello function'


print(hello_func())
print(hello_func().upper())


# EXAMPLE 3:- Passing Arguments into our FUNCTIONS

def hello_func(salutation):
    return '{} world!'.format(salutation)


print(hello_func('Hi'))


# EXAMPLE  4:-

def hello_func(salutation, name):
    return '{} {}'.format(salutation, name)


print(hello_func('Hi', 'Rudy'))


# EXAMPLE 5:- Setting a default value in a function

def hello_func(salutation, name='You'):             # Sets name='You' as default value...
    return '{} {}'.format(salutation, name)


print(hello_func('Hi'))


# EXAMPLE 6:-

def hello_func(salutation, name='You'):                # Sets name='You' as default value
    return '{} {}'.format(salutation, name)


print(hello_func('Hello', name='Nonso'))               # Unsets the default value using: name='Nonso'


# EXAMPLE 7:-

def get_gender(sex="Unknown"):
    if sex is "m":
        sex = "Male"
    elif sex is "f":
        sex = "Female"

    print(sex)


get_gender("m")
get_gender("f")
get_gender()
