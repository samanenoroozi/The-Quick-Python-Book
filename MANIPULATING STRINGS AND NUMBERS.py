import math,cmath
x=7
y=9.5
z=3+2j
a="spring"
print(a*x)
print(a*y) #TypeError: can't multiply sequence by non-int of type 'float'
print(a*z) #TypeError: can't multiply sequence by non-int of type 'complex'

print(math.sqrt(x))
print(math.sqrt(y))
print(math.sqrt(z)) #TypeError: must be real number, not complex
print(cmath.sqrt(x))
print(cmath.sqrt(y))
print(cmath.sqrt(z))
