# Finding index of a tuple also checking the
#  immutability of a tuple
a= (1,7,9,7,9)
print(a.index(7))
a[0]= 11 
# the above function returns type error
#  proving tuple is immutable