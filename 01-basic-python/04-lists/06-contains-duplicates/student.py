# Write your code here
def contains_duplicates(xs):
    for i, x in enumerate(xs):
        for y in xs[i+1:]:
            if x == y: 
                return True
    return False