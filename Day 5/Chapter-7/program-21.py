# A program to find the grade of a student from
#  marks
marks= int(input("Enter the marks of the student "))
if(marks >=90 and marks<=100):
    print("Excellent grade A+")
elif(marks>=80 and marks<90):
    print("Grade A")
elif(marks >=70 and marks <80):
    print("Grade B")
elif(marks>=60 and marks<70):
    print("Grade C")
elif(marks<60):
    print("Grade D")
else :
    print("invalid input")    

