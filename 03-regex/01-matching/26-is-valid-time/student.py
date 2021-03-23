import re

def is_valid_time(string):
    return re.fullmatch(r'[0-1]\d:[0-5]\d:[0-5]\d(\.\d{3})?', string)