def calculate_avg(marks):
    total = sum(marks)
    average = total / len(marks)
    return average  

# taking input of numbers
marks = []
input_count = 5
for i in range(input_count):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)
    
# calculating average
average = calculate_avg(marks)
print("The average marks are:", average)