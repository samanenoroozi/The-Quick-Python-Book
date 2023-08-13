#Suppose that you have a list of strings in which some (but not necessarily all)
#of the strings begin and end with the double quote character:
#What code would you use on each element to remove just the double quotes?

x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']
new = [item.replace('"', '') for item in x]
print (new)

new = [item.strip('"') for item in x]
print (new)

#What code could you use to find the position of the last p in Mississippi?

x = "Mississippi"
print (x.rindex('p'))

#When you’ve found that position, what code would you use to remove
#just that letter? 

x = "Mississippi"
print (x.replace('p', '', 1))   # perform replacement once
# I dont have another way
