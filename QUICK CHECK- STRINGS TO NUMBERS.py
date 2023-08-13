#Which of the following will not be converted to numbers, and why?

print (float("12345678901234567890"))

print (int('a1'))  #ValueError: invalid literal for int() with base 10: 'a1'

print (int('12G', 16)) #ValueError: invalid literal for int() with base 16: '12G'

print (int("12*2"))  #ValueError: invalid literal for int() with base 10: '12*2'
