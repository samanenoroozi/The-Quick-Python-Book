#What code could you use to get a copy y of that list in which
#you could change the elements without the side effect of
#changing the contents of x?

x=[[1,2,3],[4,5,6],[7,8,9]]
y = x[:]
import copy
y = copy.deepcopy(x)
print(y)
y[1]=[2,6,1]
print(y)
print(x)
