import math
from student import Student


def linear_search(students:list[Student], target_id):
    for student in students:
        if student.id == target_id:
            return student
    return None

def binary_search(students:list[Student], target_id):
    if students == []:
        return None
    
    middle = math.floor(len(students)/2)
    middle_student = students[middle]
    
    if middle_student.id == target_id:
        return middle_student
    if target_id < middle_student.id:
        return binary_search(students[:middle], target_id)
    else:
        return binary_search(students[middle+1:], target_id)