# EXAMPLE:- SET COMPREHENSIONS.....

nums = [1, 2, 4, 3, 2, 8, 9, 1, 5, 6, 3, 11, 15, 13, 11, 19]

my_set = set()
for m in nums:
    my_set.add(m)
print(my_set)

# OR in its shorter form: as in a set Comprehension.....
my_set = {m for m in nums}
print(my_set)
