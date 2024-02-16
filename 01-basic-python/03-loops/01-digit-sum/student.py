# Write your code here
def last_digit(n):
    return n%10
def remove_last_digit(n):
    return n//10
def digit_sum(n):
    # if n>=10: return last_digit(n) + digit_sum(remove_last_digit(n))
    # return n
    result = 0
    while n>0:
        result += last_digit(n)
        n = remove_last_digit(n)
    return result