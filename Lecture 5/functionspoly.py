def noReturn():
    print "Returns nothing, prints things"
    print "This is like a void function"

# int times (int x, int y) {...}

def times(x, y):
    return x * y

noReturn()

print "=================="

print "multiplying 3 with 4"
number = times(3,4)
print number

print "Calling times with fractional value"
fraction = times(3.14, 4)
print fraction

print "Times with string"
string = times("Lol" , 3)
print string
