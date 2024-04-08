# Write your code here
import re


def hide_email_addresses(string):
    def replace(match):
        return '*' * len(match.group(1))
    
    return re.sub(r'\b([a-zA-Z0-9.]+@[a-zA-Z0-9.]+)\b', replace, string)