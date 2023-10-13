'''How would you write a function that could take any number of unnamed
arguments and print their values out in reverse order?'''

def reverse(*value):
    for i in reversed(value):
        print(i)
reverse(1, 2, 3)

'''What do you need to do to create a procedure or void function—that is,
a function with no return value?'''

def shift():
    y = 8
shift()

'''What happens if you capture the return value of a function with a variable?'''

def pow(num):
    return num*num
x = pow(7)
print(x)
#output: 49



    
