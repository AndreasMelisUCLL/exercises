# Write your code here
def median(ns):
    #sort the list
    ns.sort()
    
    # if num of elements is odd, return the middle one
    if len(ns) % 2 == 1:
        return ns[len(ns)//2]
    
    # return the average of the two middle elements
    midleft = ns[len(ns)//2 - 1]
    midright = ns[len(ns)//2]
    return ( midleft + midright) / 2