# LIST COMPREHENSIONS IN PYTHON...

nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# EXAMPLE 1:- I want 'n' for each 'n' in numbers
my_list = []
for m in nums:
    my_list.append(m)
print(my_list)

# OR in its shorter form as.....
my_list = [m for m in nums]
print(my_list)


# EXAMPLE 2:- I want 'm*m' for each 'm' in numbers
my_list = []
for m in nums:
    my_list.append(m*m)
print(my_list)

# OR in its shorter form as.....
my_list = [m*m for m in nums]
print(my_list)


# EXAMPLE 3:- Using map + Lambda
my_list = map(lambda m: m*m, nums)
print(my_list)


# EXAMPLE 4:- Using filter + Lambda
my_list = filter(lambda m: m % 2 == 0, nums)
print(my_list)


# EXAMPLE 5:- I want 'm' for each 'm' in nums, if 'm' is even
from operator import attrgetter
nums = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

my_list = []
for m in nums:
    if m % 2 == 0:
        my_list.append(m)
print(my_list)

# OR in its shorter form if 'm' is odd.....
my_list = [m for m in nums if m % 2 == 1]
print(my_list)


# EXAMPLE 6:- I want a (letter, num) pair for each letter in 'abcd' & each number in "0123"
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))
print(my_list)

# OR in its shorter form.....
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)
