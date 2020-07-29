# EXAMPLE 1:-

try:
    n = open('datafile.txt')
except Exception:
    print("Error 99! This file doesn't exist!")

# OR
try:
    n = open('pro.txt')
    var = off_var
except FileNotFoundError:                          # Gives normal python Traceback....
    print("Error 99! This file doesn't exist!")
except Exception:                                  # Gives the General exception error..
    print("Sorry! We cannot find what you're looking for.")


# OR
try:
    n = open('pro_file.txt')
except FileNotFoundError as c:
    print(c)
except Exception as c:
    print(c)


# EXAMPLE 2:- # The 'else' clause only runs if there's no error/an exception isn't thrown
try:
    n = open('pro.txt')
except FileNotFoundError as c:
    print(c)
except Exception as c:
    print(c)
else:
    print(n.read())
    n.close()


# EXAMPLE 3:- The "finally" clause...
# The 'finally' clause is used regardless of whether or not the code is successful
# It's used to properly close down certain things especiallly Databases...

try:
    n = open('pro_file.txt')
except FileNotFoundError as c:
    print(c)
except Exception as c:
    print(c)
else:
    print(n.read())
    n.close()
finally:
    print("Databases currently closed down")


# EXAMPLE 4:- To Manually Raise Exceptions in Python...

try:
    n = open('pro2.txt')
    if n.name == 'pro2.txt':
        raise Exception
except FileNotFoundError as c:
    print(c)
except Exception as c:
    print('Sorry! [Error 321]')
else:
    print(n.read())
    n.close()
finally:
    print("Databases currently closed down.....")
