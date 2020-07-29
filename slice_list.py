# EXAMPLE 1:- list(start:end)
my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]

print(my_list[:])
print(my_list[3:9])
print(my_list[-11:-6])
print(my_list[5:-1])
print(my_list[:-7])
print(my_list[6:])


# EXAMPLE 2:- list(start:end:step)
print(my_list[3:-4:1])             # step ':1' doesn't skip any value in list
print(my_list[-13:7:2])            # step ':2' skips one value & O/p the next
print(my_list[-1:2:-1])            # step ':-1' doesn't skip any value in list
print(my_list[-1:2:-3])            # step '-3' skips 2 values & O/p the third
print(my_list[::-3])
