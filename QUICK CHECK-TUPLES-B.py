#B: If you had a tuple x = (3, 1, 4, 2), how might you end up with x sorted?

x=(3,1,4,2)
y=sorted(x)
print(y)    #print list


x=(3,1,4,2)
y=sorted(x)
y=tuple(y)
print(y)    #print tuple
