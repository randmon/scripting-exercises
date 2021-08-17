import re
from datetime import datetime

def by_date(string):
    m = re.search(r'Date:\s*(.*)', string)
    date = m.group(1)
    return datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

with open('input.txt') as input:
    data = input.read()

commits = re.findall(r'commit.*?Closed \#\d+', data, re.DOTALL)
# re.DOTALL
# Make the '.' special character match any character at all, including a newline;
# without this flag, '.' will match anything except a newline. 
        
commits.sort(key=by_date, reverse=True)

print("\n\n".join(commits))
#206dfaadb505514563c8