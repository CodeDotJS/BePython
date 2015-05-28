if __name__ == '__main__':
    print 'This program is being run by itself'
else:
    print 'I am being imported from another module'

# how to run this code ? 

# solution : cd /you_dir/module_using_name.py 
# here you get the result : 'This program is being run by itself

# now for printing the second part : cd /your_dir/ python -c "import module_using_name' 
# here you get the result : ' I am being imported from another module'
