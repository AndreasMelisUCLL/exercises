# Write your code here
import re


def is_valid_password(string):
    required_patterns = [
        r'.{12}',
        r'[0-9]',
        r'[a-z]',
        r'[A-Z]',
        r'[\+\-\*\/\.@]'
    ]
    
    if not all([re.search(pattern, string) for pattern in required_patterns]):
        return False
    
    invalid_patterns = [
        r'(.)\1\1',
        r'(.)(.*\1){3}'
    ]
    
    if any([re.search(pattern, string) for pattern in invalid_patterns]):
        return False
    
    return True