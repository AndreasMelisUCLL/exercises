# Write your code here
def create_dictionary(keys, values):
    dictionary = {}
    for key, value in zip(keys, values):
        dictionary[key] = value
    return dictionary