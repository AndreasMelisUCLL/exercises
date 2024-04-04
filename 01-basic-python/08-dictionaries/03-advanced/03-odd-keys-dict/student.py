# Write your code here
def odd_keys_dict(dictionary:dict):
    return dict([
        (key, value) for (key, value) in dictionary.items() if key%2 == 1
        ])