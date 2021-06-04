y = 60
x = y - 1

#while loop will fugre out if a give number is prime or not

while x > 1:
    if y % x == 0:
        print y, "has a factor in ", x
        break
    x = x - 1
else:
    print y, "is a prime number"
