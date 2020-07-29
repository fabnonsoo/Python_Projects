# CHALLENGE/HOMEWORK 4:- Write a program that computes the health rating of an individual based on their age, number of apples they eat per day and avocado smoked per day...

def health_rating(age, apples_ate, avocado):
    wellness = (120 - age) + (apples_ate * 3.5) + (avocado * 2)
    print(wellness)


Nonsos_rating = [27, 5, 0]
health_rating(Nonsos_rating[0], Nonsos_rating[1], Nonsos_rating[2])
health_rating(*Nonsos_rating)
