"""Store student names as keys and marks (list of integers) as values in a dictionary. Compute
each student’s average and grade (A/B/C/D). Print the top 2 students based on average marks."""

students={
    "Ram":[80,90,85,79,68],
    "Hari":[79,78,67,99,100],
    "Sita":[88.5,7,66,100,55.5],
    "Gita":[99,88,77,66,55]
}

def calculateGrade(avg):
    if avg>=90:
        return "A"
    elif avg>=85:
        return "A-"
    elif avg>=80:
        return "B+"
    elif avg>=75:
        return"B"
    elif avg>=70:
        return"B-"
    else:
        return"C+"

averages={}

for student, marks in students.items():
    avg = sum(marks) / len(marks)
    grade = calculateGrade(avg)
    averages[student] = avg
    print(f"{student}: Average = {avg:.2f}, Grade = {grade}")

top_students = sorted(averages.items(), key=lambda y: y[1], reverse=True)

print("\nTop 2 students based on average marks:")
for student, avg in top_students[:2]:
    print(f"{student} with average {avg:.2f}")

 



