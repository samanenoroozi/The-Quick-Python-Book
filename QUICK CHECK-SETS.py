#If you were to construct a set from the following list,
#how many elements would the set have?

x=set([1,2,5,1,0,2,3,1,1,(1,2,3)])
print(len(x))

x={[1,2,5,1,0,2,3,1,1,(1,2,3)]}
print(len(x))  #TypeError: unhashable type: 'list'
