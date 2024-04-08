# Write your code here
import re


def remove_repeated_words(string):
    return re.sub(r'(\b\w+\b)(\s\1)+', r'\1', string)