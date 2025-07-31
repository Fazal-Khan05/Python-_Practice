def calculate_avg(marks):
    total = sum(marks)
    average = total / len(marks)
    return average  

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
    print(f"The average marks for {student_name} are:", average)
   
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    print(f"Grade for {student_name}: {grade}")

