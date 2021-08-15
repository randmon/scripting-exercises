import re
import itertools

letters = sorted("QWERTYUIOP") #Needs to be in alphabetical order
passwords = itertools.product(letters, repeat=6)
for p in passwords:
    pw = "".join(p)
    if re.search(r'([EIOU])\1', pw) and re.search(r'([QWRTYP])\1', pw) and len(set(pw)) == 4:
        print(pw)
#d6f79dbf004aa2c08232572e36