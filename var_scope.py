# VARIABLE SCOPE: UNDERSTANDING THE LEGB RULE AND GLOBAL NON-LOCAL STATEMENTS.
'''
LEGB
Local, Enclosing, Global, Built-In
'''

# EXAMPLE 1:-
x = 'global x'


def vtest():
    y = 'local y'
    print(y)
    print(x)             # O/p the result because it's a global variable (not under any function)


vtest()
print(y)               # Gives an error because it's a local variale (under a function)
print(x)


# EXAMPLE 2:
# Here, the variable x is a global scope because it's not created inside any function
# Whenever a variable is created inside a function, only that function that created it can access it!
# Therefore diverse functions can access it...

x = 3647


def golden():
    print(x)


def bolden():
    print(x)


golden()
bolden()


# EXAMPLE 3:-
def tolden():
    a = 168
    print(a)


def rolden():      # This function cannot acccess the variable a because it's only created inside def tolden()
    print(a)


tolden()           # When called, it prints/outputs 168
rolden()           # When called, it gives an error/traceback



# EXAMPLE 4:- Using the Global Variable in a Function...
def vtest():
    global x                    # Global variale now used in a function...
    x = 'local x'
    print(x)


vtest()                        # Calls the function for local variale: print(x)
print(x)                       # O/p the x = 'local x' global variale


# EXAMPLE 5:-
def vtest(z):
    x = 'local x'
    print(z)


vtest('local z')


# EXAMPLE 6:- The Built-In Scope....
import builtins


def min_num():
    pass


m = [7, 14, 23, 32, 21, 15]
print(min(m))


# EXAMPLE 7i:- THE ENCLOSING SCOPE....
def outer():
    x = 'outer x'

# This is a local scope function 'def inner()' in a global function 'def outer()'
# Hence, if the x = 'inner x' is commented out/removed from the program, it O/p: outer x
# But when it's included in the program, it outputs: inner x

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)


outer()


# EXAMPLE 7ii:-
def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        x = 'inner x'
        print(x)

    inner()
    print(x)             # O/p result: 'inner x' twice because of the 'nonlocal x'


outer()


# EXAMPLE 7iii:-
x = 'global x'


def outer():
    # x = 'outer x'

    def inner():
        # x = 'inner x'
        print(x)

    inner()
    print(x)


outer()
print(x)
