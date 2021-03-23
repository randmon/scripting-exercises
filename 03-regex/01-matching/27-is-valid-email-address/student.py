import re

def is_valid_email_address(string):
    return re.fullmatch(r'[a-z\d\.]+@(student\.)?ucll\.be', string)