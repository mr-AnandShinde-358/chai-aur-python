marks=654


""" if marks >100:
    print("wrong rating")
elif marks >=90:
    print("A")
elif marks >=80:
    print("B")
elif marks >=70:
    print("B")
elif marks >=60:
    print("D")
else:
    print("F")
    """ 

if marks >=101:
    print("Please verify your grade again")
    exit()


if marks >=90:
    grade = "A"
elif marks >=80:
    grade = "B"
elif marks >=70:
    grade = "B"
elif marks >=60:
    grade = "D"
else:
    grade = "F"

print("Grade is",grade)