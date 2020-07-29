# SETS IN PYTHON:-
# Know that Sets uses Curly braces {}
# Removes duplicate values
# You can find similarities in Sets

# EXAMPLE 1:-

data_courses = {'Math', 'Machine Learning', 'OpResearch', 'Statistics', 'Math'}
print(data_courses)


# EXAMPLE 2:- Finding similarities in Sets;

data_courses = {'Math', 'Machine Learning', 'OpResearch', 'Statistics'}
cs_courses = {'Assembly Lang', 'Physics', 'Math', 'Statistics'}
print(data_courses.intersection(cs_courses))


# EXAMPLE 3:- Finding a value in one set that is not in another set;

data_courses = {'Math', 'Machine Learning', 'OpResearch', 'Statistics'}
cs_courses = {'Assembly Lang', 'Physics', 'Math', 'Statistics'}
print(data_courses.difference(cs_courses))


# EXAMPLE 4:- Finding the combination of all values in both sets;

data_courses = {'Math', 'Machine Learning', 'OpResearch', 'Statistics'}
cs_courses = {'Assembly Lang', 'Physics', 'Math', 'Statistics'}
print(cs_courses.union(data_courses))


# EXAMPLE 5:-

groceries = {"lotion", "cereal", "biscuits", "chocolates", "milk", "wine", "fruit juice", "cereal"}     # This line eliminates one of the cereal in the sets...
print(groceries)

if "wine" in groceries:
    print("Thank God I've got wine!")
else:
    print("Nonso, you need to stock your fridge with good wine")
