# Write your code here
def remove_duplicates(xs):
    seen = set()
    ys = []
    for x in xs:
        if x not in seen:
            ys.append(x)
            seen.add(x)
    return ys