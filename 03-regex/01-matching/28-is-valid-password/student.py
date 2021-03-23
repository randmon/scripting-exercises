import re

def is_valid_password(string):
    r = ['.{8,}', r'\d', '[a-z]', '[A-Z]', r'[-+/.*@]']
    n = [r'(.)\1{2}', r'(.)(.*\1){3}']

    return all(re.search(regex, string) for regex in r) and not any(re.search(regex, string) for regex in n)