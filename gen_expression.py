nums = [1, 2, 4, 3, 2, 8, 9, 1, 5, 6, 3, 11, 15, 13, 11, 19]


def gen_func(nums):
    for m in nums:
        yield m*m


my_gen = gen_func(nums)
for x in my_gen:
    print(x)


# OR in its shorter form: as in a Generator Comprehension.....
my_gen = (m*m for m in nums)
for x in my_gen:
    print(x)
