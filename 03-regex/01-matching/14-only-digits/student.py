import re

def only_digits(string):
    return re.fullmatch('\d*', string)