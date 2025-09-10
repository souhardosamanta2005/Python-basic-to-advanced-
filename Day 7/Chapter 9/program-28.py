# To convert celcius to farenheit using functions 
def cel_to_faren(f):
    return (c*9/5)+32
c= int(input("Enter the temperature in celcius "))
f= cel_to_faren(c)
print(f"{round(f,2)} degree farenheit")

