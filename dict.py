# DICTIONARY IN PYTHON......

# EXAMPLE 1:

student = {'name': 'John', 'age': 23, 'courses': ['Statistics', 'CompSci']}
print(student)
print(student['courses'])

# To Return a key that doesn't exist, thereby preventing a traceback, we use 'get'
print(student.get('address'))         # Returns 'None' without a traceback


# EXAMPLE 2:-

# Lets specify a default value for keys that don't exist;
student = {'name': 'John', 'age': 23, 'courses': ['Statistics', 'CompSci']}
print(student.get('phone', 'Not Found'))


# To add a new entry/key to the dict....;
student = {'name': 'Nancy', 'age': 23, 'courses': ['Statistics', 'CompSci']}
student['City'] = 'Seattle, WA'
student['name'] = 'Kellyanne'         # Updates the key - from 'Nancy' to 'Kellyanne'
print(student)


# To Update/add multiple entries into our dict:-
student.update({'name': 'Victor', 'address': 'Boston, MA', 'phone': '432-67998'})
print(student)


# EXAMPLE 3:- To Delete a specific key:value;

student = {'name': 'John', 'age': 23, 'courses': ['Statistics', 'CompSci'], 'city': 'Toronto'}
del student['age']
print(student)


# Another way to remove a key:value;.....
city = student.pop('city')
print(student)
print(city)


# EXAMPLE 4:-

student = {'name': 'John', 'age': 23, 'courses': ['Statistics', 'CompSci'], 'city': 'Toronto'}

print(len(student))                # Gives the number of key:value pairs
print(student.keys())              # Gives the keys in our dict...
print(student.values())            # Gives the values in our dict...
print(student.items())             # Gives all the k:v in our dict...


# To loop through the key:value pairs;
for key, value in student.items():
    print(key, value)


# EXAMPLE 5:-

coursemates = {"Nkem": "was the best graduating student", "Raph": " is Brilliant but cheats", "Melody": " can be troublesome"}

print(coursemates)
print(coursemates["Melody"])

for k, v in coursemates.items():
    print(k + v)
