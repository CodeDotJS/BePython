# This is a string object
name = 'Rishi'

if name.startswith('Swa'):
    print 'Yes, the string starts with "Ris"'

if 'i' in name:
    print 'Yes, it contains the string "i"'

if name.find('shi') != -1:
    print 'Yes, it contains the string "war"'

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print delimiter.join(mylist)

