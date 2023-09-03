'''you need to remove all negative numbers from
that list. Write the code to do this.'''

x = [1, 3, 5, 0, -1, 3, -2]
for i, n in enumerate(x):
    if n < 0:
        del x[i]
print(x)

x = [item for item in x if item >= 0]
print (x)


'''How would you count the total number of negative numbers in a list'''

y = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]
total = 0
for a in y:
    for b in a:
        if b < 0:
            total += 1
print(total)

'''What code would you use to print very low if the value of x is below -5,
low if it’s from -5 up to 0, neutral if it’s equal to 0,
high if it’s greater than 0 up to 5, and very high if it’s greater than 5?'''

x = 3

if x < -5:
    print("very low")
elif -5 < x < 0:
    print("low")
elif x == 0:
    print("neutral")
elif 0 < x < 5:
    print ("high")
elif x > 5:
    print("very high")
else:
    print("none")
