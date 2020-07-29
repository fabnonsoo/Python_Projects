# LIST IN PYTHON.....

# EXAMPLE 1:-

courses = ['Math', 'Robotics', 'OpResearch', 'Physics']

print(len(courses))
print(courses[0])
print(courses[-1])
print(courses[:2])
print(courses[2:])


# EXAMPLE 2:-

courses = ['Math', 'Robotics', 'OpResearch', 'Physics']

courses.append('Statistics')
courses.insert(1, 'Machine Learning')
print(courses)

courses_1 = ['Education', 'Probability', 'Art']
courses.extend(courses_1)
print(courses)


# EXAMPLE 3:-

courses = ['Math', 'Robotics', 'OpResearch', 'Physics']
courses.remove('Robotics')
print(courses)

courses.pop()               # Removes a value and O/p remaining values in the list
print(courses)

# OR

tina = courses.pop()        # Gives you the value in the list that was removed
print(tina)


# EXAMPLE 4:-

courses = ['Math', 'Robotics', 'OpResearch', 'Physics']

courses.reverse()          # Reverses the values in list from right to left
print(courses)

courses.sort()             # Sorts our list in alphabetical/ascending order
print(courses)


# EXAMPLE 5:-

nums = [2, 4, 6, 8, 10, 12]
courses = ['Math', 'Robotics', 'OpResearch', 'Physics']

nums.sort()                  # Sorts our numbers list in ascending order
print(nums)


# Sorting our nums and courses lists in descending order, we say:-
courses.sort(reverse=True)
nums.sort(reverse=True)
print(courses)
print(nums)


# Getting sorted version of our list without altering the original list
sorted_courses = sorted(courses)
print(sorted_courses)


# EXAMPLE 6:-

nums = [2, 4, 6, 8, 10, 12]
courses = ['Math', 'Robotics', 'OpResearch', 'Physics']

print(min(nums))
print(max(nums))
print(sum(nums))

print(courses.index('Physics'))         # O/p the index of Physics in the list
print('Robotics' in courses)            # O/p a True/False of Robotics value in the list


for course in courses:
    print(course)


# EXAMPLE 7:-

courses = ['Math', 'Robotics', 'OpResearch', 'Physics']

for index, course in enumerate(courses):
    print(index, course)                       # O/p both the courses & its index

# To make our "course index" start at 1, we say:-
for index, course in enumerate(courses, start=1):
    print(index, course)


# EXAMPLE 8:-

# Lets change the values in our list to strings seperated by a comma/hyphen:-
courses = ['Math', 'Robotics', 'OpResearch', 'Physics']

course_lstostr = ', '.join(courses)            # Result seperated by a comma;
print(course_lstostr)

course_lstostr = ' - '.join(courses)         # Result seperated by a hyphen;
print(course_lstostr)


# FROM STRING TO LIST;
strto_list = course_lstostr.split(' - ')
print(strto_list)
