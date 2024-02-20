# Write your code here
def target_sum(ns, target):
    for i, n1 in enumerate(ns):
        for n2 in ns[i:]:
            if n1 + n2 == target:
                return True
    return False