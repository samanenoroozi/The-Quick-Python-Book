'''Rewrite the word-count program from section 8.7 to make it shorter.
You may want to look at the string and list operations already discussed,
as well as think about different ways to organize the code. You may also
want to make the program smarter so that only alphabetic strings
(not symbols or punctuation) count as words.'''

#!/#usr/bin/env python3

""" Reads a file and returns the number of lines, words,
and characters ­ similar to the UNIX wc utility
"""

infile = open('word_count.tst') 
lines = infile.read().split("\n") 
line_count = len(lines) 
word_count = 0 ;char_count = 0 

for line in lines: 
    word_count += len(line.split() )
    char_count += len([c for c in line if c.isalpha()])

print("File has {0} lines, {1} words, {2} characters".format
(line_count, word_count, char_count))
