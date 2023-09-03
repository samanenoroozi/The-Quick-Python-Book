'''What list comprehension would you use to process
the list x so that all negative values are removed?'''

x = [5, 1, -2, 0, -7, 3, -4]
x = [item for item in x if item>=0]
print(x)


'''Create a generator that returns only odd numbers from 1 to 100.'''

generator = (i for i in range(0, 100) if i%2 == 1)
for i in generator:
    print(i, end = ",")


'''Write the code to create a dictionary of the numbers
and their cubes from 11 through 15.'''

y = {item:item**3 for item in range(11,16)}
print("\n", y)
