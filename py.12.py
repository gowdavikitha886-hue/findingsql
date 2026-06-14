# Student Grade Management System

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details for student {i + 1}")
    name = input("Name: ")
    marks = []

    for j in range(3):
        mark = float(input(f"Enter subject {j + 1} mark: "))
        marks.append(mark)

    total = sum(marks)
    average = total / 3

    if average >= 90:
        grade = "A+"
    elif average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "Fail"

    students.append([name, marks, total, average, grade])

print("\n--- Student Report ---")
for s in students:
    print("\nName:", s[0])
    print("Marks:", s[1])
    print("Total:", s[2])
    print("Average:", s[3])
    print("Grade:", s[4])