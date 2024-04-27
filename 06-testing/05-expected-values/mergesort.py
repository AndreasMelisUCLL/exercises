def split_in_two(ns):
    i = round(len(ns) / 2)
    return ns[:i], ns[i:]


def merge_sorted(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    return result + left[i:] + right[j:]


def merge_sort(ns):
    if len(ns) <= 1:
        ns = list(ns)
        return ns
    
    left, right = split_in_two(ns)
    sorted_left, sorted_right = merge_sort(left), merge_sort(right)
    
    return merge_sorted(sorted_left, sorted_right)
    