#What would be a quick way to change all punctuation in a string to spaces?

import string

x = 'what is (your) name?'
y = x.translate(str.maketrans('', '', string.punctuation))

print(y)
