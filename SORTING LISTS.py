#If you wanted to sort this list by the second element in each list,
#what function would you write to pass as the key value to the sort() method? 

def sort(x):
    return(sorted(x,key=lambda x:x[1]))
x=[[1,3,0],[4,2,1],[2,0,3]]

print(sort(x))
