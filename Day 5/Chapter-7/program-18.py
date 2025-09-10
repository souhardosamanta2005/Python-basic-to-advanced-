# If , Else, Elif
# A program to find greatest of four numbers 
# entered by the user
a= int(input("enter yopur first number "))
b= int(input("enter your second number "))
c= int(input("enter your third number "))
d= int(input("enter your fourth number "))

if (a>b and a>c and a>d):
    print(a)
elif (b>a and b>c and b>d):
    print(b)
elif (c>a and c>b and c>d):
    print(c)
else:
    print(d)


