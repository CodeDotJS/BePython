def func(a, b=5, c=10):
    print 'a is', a, 'and b is', b, 'and c is', c

func(3, 7) # a is 3
func(25, c=24) # a is 25 and b is 5
func(c=50, a=100) # a is 100, b is 5 , c is : 50

