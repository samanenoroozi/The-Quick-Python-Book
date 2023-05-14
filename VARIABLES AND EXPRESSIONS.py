#What happens when you try to put spaces, dashes, or other nonalphanumeric characters in the variable name?

-x=7 #SyntaxError: cannot assign to expression here.
x/=7 #NameError: name 'x' is not defined
/x=7 #SyntaxError: invalid syntax
 x=7 #SyntaxError: unexpected indent
2x=7 #SyntaxError: invalid decimal literal
x!=7 #False
x !=7 #False
x /=7 #False

x2=7 #True
_x=7 #TRue

#Play around with a few complex expressions, such as x = 2 + 4 * 5 – 6 / 3. Use parentheses to group the numbers in different ways and see how the result changes compared with the original ungrouped expression.

x=(2+4)*(5-6)/3
y=2+4*(5-6)/3
z=2+4*5-6/3
print(x,y,z)
