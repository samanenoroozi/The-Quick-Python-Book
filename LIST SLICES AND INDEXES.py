#how would you combine the len()function and list slices to get the second half of a list when you don’t know what size it is?

x=[1,2,3,4,5,6,7,8,9,10]
a=x[len(x)//2:]

def split_list(x):
    half = len(x)//2
    return x[half:]

print (a)
