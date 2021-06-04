def func(x,y,z):
    return x + y + z

l = lambda x = 10, y = 20, z = 30 : x + y + z

print "Calling lambda with no arguments uses defaults"
print l()
print "This will use the inputted 3 arguments"
print l(5,6,7)
print "This will use the first 2 given and then use default for the third"
print l(1,2)
