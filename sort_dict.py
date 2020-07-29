# EXAMPLE 1:- Sorts out the keys....

dict = {'name': 'Nonso', 'school': 'Univ of Washington', 'age': None, 'city': 'Toronto'}
s_dict = sorted(dict)
print(s_dict)


# EXAMPLE 2:-
list = [-7, -6, -5, 3, 2, 1]
s_list = sorted(list)
s_list = sorted(list, reverse=True)         # Outputs in descending order....
s_list = sorted(list, key=abs)              # Sorting using 'absolute value key
print(s_list)
