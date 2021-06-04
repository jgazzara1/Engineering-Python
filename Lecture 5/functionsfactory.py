def powerOf(N):
    def coreAct(x):
        return x**N
    return coreAct

print "====="
print "Raised to 2"
f = powerOf(2) #f is now a label, pointing to a binary wihich is able to raise arguments to the power of 2
print f(3)
print f(4)

print "======"
print "Raised to 3"

g = powerOf(3)
print g(2)
print g(3)
