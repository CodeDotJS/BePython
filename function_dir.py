import sys 

# get names of attributes in sys module
print dir(sys)

# get names of attributes for current module
print dir()

# creating a new variable a
a = 5 
print dir()

# deleting / removing a name
del a 
print dir()

print dir(print)

print dir(str)
