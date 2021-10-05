import timeit


SETUP = '''
import random
a_list = [i for i in range(1,10000000)]
random_ints = [random.randrange(10000000) for i in range(1000)]
a_set = {i for i in range(1, 10000000)}
'''
STMT_list= '''
found = 0
for i in random_ints:
    if i in a_list:
        found +=1
'''
STMT_set = '''
found = 0
for i in random_ints:
    if i in a_set:
        found +=1
'''

time_1 = timeit.timeit(stmt=STMT_list, setup=SETUP, number=1)
time_2 = timeit.timeit(stmt=STMT_set, setup=SETUP, number=1)

print(f'Look up 1000 random number in a list with 10000000 items takes {time_1}s')
print(f'Look up 1000 random number in a set with 10000000 items takes {time_2:0.10f}s')
