# EXAMPLE 1:- DICTIONARY COMPREHENSIONS....

hero_names = ['Jon Snow', 'Peter', 'Wade', 'Bruce', 'Logan', 'Clark', 'Klaus']
movies = ['GOT', 'Spiderman', 'Deadpool', 'Batman', 'Wolverine', 'Superman', 'Originals']

print zip(hero_names, movies)              # Results in a tuple of key:value pairs

my_dict = {}
for hero_names, movies in zip(hero_names, movies):
    my_dict[hero_names] = movies
print(my_dict)                             # Results in a dict of key:value pairs


# OR in its shorter form: as in a dict{} Comprehension.....
my_dict = {hero_names: movies for hero_names, movies in zip(hero_names, movies)}
print(my_dict)


# EXAMPLE 2:- If 'hero_names' not eaqual to 'Logan' -> eliminates Logan from the dict...
my_dict = {hero_names: movies for hero_names, movies in zip(hero_names, movies) if hero_names != 'Logan'}
print(my_dict)
