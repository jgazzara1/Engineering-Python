#this is a grade calculator
#homeworks 30% of grade, midterms 40%, and final project is 30%
#figuring out the letter grade

homework = int(raw_input("Enter homework score:" ))
midterm = int(raw_input("Cumulative midterm score:" ))
project = int(raw_input("Emter project score:" ))

finalScore = 0.3*homework + 0.4*midterm + 0.3*project

print "Final score: ", finalScore 

#lets map this final score to a letter grade
# if FS >= 90, A
# and is actually redundant here

if finalScore >= 90:
    print "A"
elif finalScore >= 80 and finalScore < 90:
    print "B"
elif finalScore >= 70 and finalScore < 80:
    print "C"
else:
    print "D :/"
