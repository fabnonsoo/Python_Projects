# LOOPS AND ITERATIONS - FOR/WHILE LOOPS AND RANGE IN PYTHON....


# EXAMPLE 1:-

nums = [2, 4, 6, 8, 9, 10]

for num in nums:
    if num == 8:
        print('Number Found!')
        break
print(num)


# EXAMPLE 2:-

nums = [2, 4, 6, 8, 9, 10]

for num in nums:
    for letter in 'abc':
        print(num, letter)


# EXAMPLE 3:-

for n in range(10):
    print(n)

for i in range(1, 11):
    print(i)


# WHILE LOOP IN PYTHON....

# EXAMPLE 1:-

x = 0

while x < 10:
    print(x)
    x += 1


# EXAMPLE 2:-
x = 0

while x < 10:
    if x == 7:
        break
    print(x)
    x += 1


# EXAMPLE 3:-
x = 2

while True:
    if x == 12:
        break
    print(x)
    x += 2


# EXAMPLE 4:-

passinggrade = 3.0

while passinggrade < 5.0:
    passinggrade += 0.5
    print(passinggrade)


# RANGE IN PYTHON....

# EXAMPLE 1:

for y in range(10):
    print(y)


# EXAMPLE 2:

for y in range(4, 12):
    print(y)


# EXAMPLE 3:

for y in range(10, 50, 5):
    print(y)


# EXAMPLE 4:

for y in range(5):
    print("Nonso is Awesome")


# EXAMPLE 5:-
magicNumber = 36

# This Program finds a magic number....

for n in range(101):
    if n is magicNumber:
        print("The magic number is: ", n)
        break
    else:
        print(n)


# EXAMPLE 6:-

jerseyNum = [2, 5, 8, 12, 15, 18, 19]

for b in range(1, 20):                    # This line loops through 1 to 20...
    if b in jerseyNum:
        continue
    print(b)
