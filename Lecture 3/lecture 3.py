while True:
    reply = raw_input("Enter text:")
    if reply == 'stop' : break

    try:
        num = int(reply)
    except:
        print "Oopsy woopsie me made a fucky wucky"
    else:
        print "Working correctly"

print "Bye"
