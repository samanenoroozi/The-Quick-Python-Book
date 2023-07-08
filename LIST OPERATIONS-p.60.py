#What would be the result of len([[1,2]] * 3)?

print(len([[1,2]]*3))


#What are two differences between using the in operator and a list’s index() method?

x=[4,0,-4,"one",3,4]
print(x.index(4))
print(3 in x)


#Which of the following will raise an exception?

print(min(["a","b","c"]))
print(max([1,2,"three"]))  #TypeError: '>' not supported between instances of 'str' and 'int'
x=[1,2,3]
print(x.count("one"))
