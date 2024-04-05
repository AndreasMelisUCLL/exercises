import re


def parse_time(string):
    match = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(?:[:|\.](\d{3}))?', string)

    if match:
        return tuple([int(group) for group in match.groups('0')])
    
    return None