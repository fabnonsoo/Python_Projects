# WRITING FILES IN PYTHON.....


# If you writing to a file that doesn't exist, it'll create it...
# If you writing to a file that does exist, it'll overwrite it...
# Incase you don't want to overwrite an existing file, you use 'a' to append

# EXAMPLE 1:- WRITING TO FILES IN PYTHON....
fv = open('pro.txt', 'w')
fv.write("The actions of a lot of African leaders are corrupt and no one is holding them accountable!\n")
fv.write("This has resulted in Blacks being seen as irrelevant or second class citizens in every place they find themselves\n")
fv.write("Especially in the White predominantly regions of the world!\n")
fv.close()


# EXAMPLE 2:-
with open('pro2.txt', 'w') as fw:
    pass                               # Creates a file without putting anything there
    fw.write('Test Python and Linear Algebra')
    fw.seek(5)                         # Replaces the 5th index with 'R' -> Rython
    fw.write('R')
