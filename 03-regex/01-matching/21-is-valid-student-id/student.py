import re

def is_valid_student_id(string):
    return re.fullmatch('[RrSs]\d{7}', string)
