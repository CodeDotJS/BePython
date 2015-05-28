# 'ab' is short for 'a'ddress'b'ook

ab = {  'Rishi'   : 'rishi@gmail.com',
        'Giri'     : 'giri@gmail.com',
        'Dotjs' : 'dotjs@gmail.com',
        'Dotpy'   : 'spammer@hotmail.com'
    }

print "Rishi's address is", ab['Rishi']

# Deleting a key-value pair
del ab['Dotpy']

print '\nThere are {} contacts in the address-book\n'.format(len(ab))

for name, address in ab.items():
    print 'Contact {} at {}'.format(name, address)

# Adding a key-value pair
ab['Guido'] = 'guido@javascript.org'

if 'Guido' in ab:
    print "\nGuido's address is", ab['Guido']

