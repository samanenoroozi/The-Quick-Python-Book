#A: why the following operations aren’t legal for the tuple x = (1, 2, 3, 4):

x=(1,2,3,4)
x.append(1)
x[1]="hello"
del x[2]
#AttributeError: 'tuple' object has no attribute 'append'
#tuple is immutable.

