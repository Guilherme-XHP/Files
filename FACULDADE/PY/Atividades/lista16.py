# Create an empty dictionary to store student information
student_dict = {}

# Read the name and average grade of the student
name = input("Enter the student's name: ")
average_grade = float(input("Enter the student's average grade: "))

# Determine the student's situation based on the average grade
if average_grade >= 7.0:
    situation = "Aprovado"
else:
    situation = "Reprovado"

# Store the student's information in the dictionary
student_dict[name] = {"Média": average_grade, "Situação": situation}

# Print the student's information
print("Student Information:")
for name, info in student_dict.items():
    print(f"Name: {name}")
    print(f"Average Grade: {info['Média']}")
    print(f"Situation: {info['Situação']}")
    