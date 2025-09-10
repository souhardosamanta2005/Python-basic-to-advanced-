# Finding the length of a set
s= set()
s.add(678)
s.add('678')
s.add(678.0)
print(s)
# This is a classic program which explains that
# in python numerically both 678 and 678.0 are
#  same. So in set they are not two unique values.
# So the answer after running is{'678',678}