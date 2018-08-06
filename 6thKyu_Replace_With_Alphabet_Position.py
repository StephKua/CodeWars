# Welcome.

# In this kata you are required to, given a string, replace every letter with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

# a being 1, b being 2, etc.

# As an example:

# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" as a string.

from string import ascii_lowercase
from itertools import count
def alphabet_position(text):
    letters = dict(zip(ascii_lowercase, count(1)))
    ans = [str(letters[t]) for t in text.lower() if t in letters]
    return " ".join(ans)