import re

def is_number(string):
    return re.fullmatch('^\d+(\.\d+)?', string)