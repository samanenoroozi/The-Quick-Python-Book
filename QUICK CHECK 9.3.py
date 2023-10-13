'''What would be the result of changing a list or dictionary that was passed
into a function as a parameter value? Which operations would be likely to
create changes that would be visible outside the function?
What steps might you take to minimize that risk?'''

list1 = [5, 7, 52, 4]
list2 = [5, 7, 52, 4]
dict1 = {1:3, 2:12, 3:6}
dict2 = {1:3, 2:12, 3:6}

def add7(x):
    x.append(7)
    print(x)

add7(list1)
print(list1)

add7(list2.copy())
print(list2)

def remove2(x):
    x.pop(2)
    print(x)

remove2(dict1)
print(dict1)

remove2(dict2.copy())
print(dict2)

