# CONDITIONALS AND BOOLEANS - IF, ELSE, ELIF STATEMENTS...


# EXAMPLE 1:-

Lang = 'C++'

if Lang == 'Python':
    print('Language is Definitely Python')
elif Lang == 'C++':
    print('Language is Definitely C++')
elif Lang == 'R':
    print('Language is Definitely R')
else:
    print('No Match!')


# EXAMPLE 2:-

user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('Access Granted')
else:
    print('Bad Credentials')


# EXAMPLE 3:-

user = 'Admin'
logged_in = False

if not logged_in:
    print('Kindly Log In')
else:
    print('Welcome!')


# EXAMPLE 4:-

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)              # Returns TRUE...
print(id(a))               # Returns the memory ID of a...
print(id(b))               # Returns the memory ID of b...
print(a is b)              # Returns 'False' because both a & b doesn't have same memory ID


# EXAMPLE 5:-

a = [4, 8, 12]
b = a

print(id(a))
print(id(b))
print(a is b)
