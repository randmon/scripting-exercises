import re

def is_valid_student_id(string):
    return re.fullmatch(r'[RrSs]\d{7}', string)
