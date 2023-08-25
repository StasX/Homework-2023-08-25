grades = []

print("Please enter 10 grades")

for i in range(1, 11):
    user_input = input(f"Grade {i}: ")
    grade = int(user_input)
    grades.append(grade)

valid_grades = []
invalid_grades = []

for grade in grades:
    if 0 <= grade <= 100:
        stringed_grade = str(grade)
        valid_grades.append(stringed_grade)
    else:
        stringed_grade = str(grade)
        invalid_grades.append(str(stringed_grade))

msg_valid = "All grades valid"
msg_invalid = "Some grades invalid.\nCheck them out!"

msg = msg_valid if len(grades) == len(valid_grades) else msg_invalid
print(msg)

print("Valid grades is", ", ".join(valid_grades))
print("Invalid grades is", ", ".join(invalid_grades))
