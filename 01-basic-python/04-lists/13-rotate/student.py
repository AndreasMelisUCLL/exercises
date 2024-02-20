# Write your code here
def rotate(xs, n):
    for _ in range(n):
        xs.append(xs.pop(0))