# EXAMPLE 1:- SORTING LISTS
list = [19, 23, 1, 3, 52, 38, 4, 7, 64, 79]


s_list = sorted(list)
print('Sorted Variable:\t', s_list)

list.sort()            # You can't do s_list = list.sort()/print(list.sort()), else you'll get a 'NONE' O/P
print('Original Variable:\t', list)


# EXAMPLE 2:- # Returning list in descending order....
s_list = sorted(list, reverse=True)
print('Sorted Variable:\t', s_list)

list.sort(reverse=True)
print('Original Variable:\t', list)
