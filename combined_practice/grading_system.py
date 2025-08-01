def calculate_avg(marks):
    total = sum(marks)
    average = total / len(marks)
    return average  

def assign_grade(average):  
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

num_students = int(input("Enter the number of students: "))
num_subjects = int(input("Enter the number of subjects: "))

for i in range(num_students):
    student_name = input(f"Enter the name of student {i + 1}: ")
    marks = []

    for j in range(num_subjects):
        mark = float(input(f"Enter marks for subject {j + 1} for {student_name}: "))
        marks.append(mark)
    
    # calculating average
    average = calculate_avg(marks)
    grade = assign_grade(average)  # get the grade

    print(f"The average marks for {student_name} are:", average)
    print(f"Grade for {student_name}: {grade}")  # print grade

with open('grades.txt', 'a') as file:
    file.write(f"Name : {student_name}, Average Marks: {average: .2f}, Grade: {grade}\n")