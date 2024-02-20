# Write your code here
def word_count(string):
    if string == "":
        return 0
    return len(string.split(' '))