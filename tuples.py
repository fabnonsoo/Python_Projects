# TUPLES IN PYTHON....

# NB: You can modify list but not TUPLES, this is known as mutable & immutable
# List uses a [], WHILE, Tuples uses a ()

# Mutable list:-
list_a = ['Math', 'Robotics', 'OpResearch', 'Physics']
list_b = list_a

print(list_a)
print(list_b)

list_a[3] = 'Machine Learning'
print(list_a)


# Immutable TUPLES:-
tuple_a = ('Math', 'Robotics', 'OpResearch', 'Physics')
print(tuple_a)

# Line 23 -> Gives TypeError: 'tuple' object does not support item assignment because tuples aren't Mutable..
# That's the difference between tuples and list..
tuple_a[3] = 'Machine Learning'
