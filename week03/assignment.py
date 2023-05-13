print()
print("Welcome to Grade Calculator 😄")

line = "--------------------------------------------------------------------------"

print(line)

grade_percentage = int(input("Please enter your grade percent: "))

if grade_percentage >= 90:
    letter = "A"
elif grade_percentage >= 80:
    letter = "B"
elif grade_percentage >= 70:
    letter = "C"
elif grade_percentage >= 60:
    letter = "D"
else:
    letter = "F"

if grade_percentage >= 93 or grade_percentage < 60:
    sign = ""
else:
    remainder = grade_percentage % 10
    if remainder < 3:
        sign = "-"
    elif remainder >= 7:
        sign = "+"
    else:
        sign = ""
    
print("Grade: " + letter + sign)

if grade_percentage >= 70:
    message = "Congratulations!!!, you passed the course 🎈⭐"
else:
    message = "Sorry, you did not get the minimum score, please re-enroll, we believe in you."
    
print(message)

print(line)