'''In processing raw text, it’s quite often necessary
to clean and normalize the text before doing anything else. If you want to
find the frequency of words in text, for example, you can make the job easier
if, before you start counting, you make sure that everything is lowercase (or
uppercase, if you prefer) and that all punctuation has been removed. You can
also make things easier by breaking the text into a series of words. In this lab,
the task is to read the first part of the first chapter of Moby Dick (found in the
book's source code), make sure that everything is one case, remove all punc-
tuation, and write the words one per line to a second file. Because I haven’t
yet covered reading and writing files, here’s the code for those operations:'''

import string

punctuation = string.punctuation
with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
    for line in infile:
        upper_lines = line.upper()
        lines = upper_lines.maketrans(punctuation, " " * len(punctuation))
        lines = upper_lines.translate(lines)
        words = lines.split()
        words = "\n".join(words)
        outfile.write(words)
