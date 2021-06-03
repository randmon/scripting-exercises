import re
#Removes repeated words that come after eachother, separated by a space
#Does not remove all the occurences of one word if they are separated by other different words
#Example: in ['a', 'b', 'a'] the 2nd 'a' is not removed
def remove_repeated_words(string):
    return re.sub(r'([a-zA-Z]+)( \1)+', r'\1', string)