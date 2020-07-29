# CHALLENGE 2: Write a program that sets the age limit for which a guy can date a girl....

def dating_age_limit(myage):
    girls_age = myage/2 + 7
    return girls_age


boys_limit = dating_age_limit(27)
Bobbys_limit = dating_age_limit(40)

print("Boys at 27 can date girls from: ", boys_limit, "or older")
print("Boys at 40 can date girls from: ", Bobbys_limit, "or older")
