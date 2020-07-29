# READING AND WRITING FILES AT THE SAME TIME IN PYTHON.....
# In order to work with images we'll open this files in binary mode..
# In otherwordS, we'll be reading and writing bytes instead of text (See ex 2).


# EXAMPLE 1:-
with open('pro.txt', 'r') as rf:
    with open('pro_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


# EXAMPLE 2:- FILE OBJECTS --> Copy an Image/Picture from our directory using File Objects in Python..

with open('482.jpg', 'rb') as rf:
    with open('482_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)


# EXAMPLE 3:- Now lets have control over the size of our image...

with open('482.jpg', 'rb') as rf:
    with open('482_copy.jpg', 'wb') as wf:
        imagechunk_size = 5000
        rf_imagechunk = rf.read(imagechunk_size)
        while len(rf_imagechunk) > 0:
            wf.write(rf_imagechunk)
            rf_imagechunk = rf.read(imagechunk_size)        # Prevents an infinite looping
