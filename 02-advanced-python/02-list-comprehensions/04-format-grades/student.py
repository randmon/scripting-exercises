from statistics import mean

def format_grades(grades):
    return "\n".join(f'{name}: {round(mean(grades))}' for name, grades in grades.items())