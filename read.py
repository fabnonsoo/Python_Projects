# FILE OBJECTS:- READING FILES IN PYTHON...

# EXAMPLE 1:-
fr = open('pro.txt', 'r')
plain_text = fr.read()
print(plain_text)
fr.close()


# EXAMPLE 2:-

fw = open('pro.txt', 'r')

print(fw.name)
print(fw.mode)
fw.close()


# EXAMPLE 3:- Reading to a File Using a Context Manager...

# The adavantage of context manager is that it helps us close the file automatically
# Within the block ('with') we're running the read code...

with open('pro.txt', 'r') as f:
    f_contents = f.read()                  # Reads the full file content
    f_contents = f.readlines()             # Reads the full file content as a list
    f_contents = f.readline()              # Reads the first line of file
    print(f_contents, end='')              # end='' - removes a new line


# EXAMPLE 4:- Reading all contents from an extremely large file...

# We do this because doing the read() from a large file all at once will make us run out of memory...
# This is efficient because it's not reading all our files at once...


with open('pro.txt', 'r') as f:
    for line in f:
        print(line, end='')


# EXAMPLE 5:- To read a specific number of lines from a text file..;;

# This helps us have administrative authority over what we want someone to see.
# When we reach the end of a file, the program just outputs an empty string

with open('pro.txt', 'r') as fw:
    fw_contents = fw.read(50)            # Reads the first 50 characters of the file..
    print(fw_contents, end='')

    fw_contents = fw.read(50)           # Reads the next 50 characters of the file..
    print(fw_contents, end='')

# OR.....

with open('pro.txt', 'r') as fw:
    size_to_read = 100
    fw_contents = fw.read(size_to_read)

    while len(fw_contents) > 0:                  # Loops through 100 characters at a time
        print(fw_contents, end='*')             # '*' helps us know when we've gotten to 100 characters
        fw_contents = fw.read(size_to_read)      # Prevents an infinite looping of the file...


# EXAMPLE 6:- Getting our current position in the file..

with open('pro.txt', 'r') as fw:
    size_to_read = 15
    fw_contents = fw.read(size_to_read)
    print(fw.tell())                          # Helps us see our current position in the file
