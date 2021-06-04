f = open("demo.txt", "r")

for x in f:
    print x
    
f = open("demo.txt", "a")
f.write("Now this file has one more line!")

f = open("demo.txt", "w")
f.write("oops we just overwrote everything in the file")
