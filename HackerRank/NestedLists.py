def find_second_lowest_names(students):
    if len(students) < 2:
        return []  
    unique_grades = sorted(set(grade for _, grade in students))

    if len(unique_grades) == 1:
        return []
    elif len(unique_grades) == 2:
        return [name for name, grade in students if grade == unique_grades[1]]
    second_lowest_grade = unique_grades[1]
    second_lowest_students = [
        name for name, grade in students if grade == second_lowest_grade
    ]
    second_lowest_students.sort()

    return second_lowest_students
num_students = int(input())
students = []
for _ in range(num_students):
    name = input()
    score = float(input())
    students.append([name, score])
    
second_lowest_names = find_second_lowest_names(students)
if second_lowest_names:
    for name in second_lowest_names:
        print(name)
else:
    print("No students with the second lowest grade")

