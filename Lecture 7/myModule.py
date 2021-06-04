_loginName = 10 #underscore prevents variable from being imported
x = 5
y = 4


def simpleFunction():
    print "This is a simple function"

def showRelatedVideos():
    print "That displays new video clips"

#================
    # A C T I O N
#================

if __name__ == "__main__":
    x = x + 7
    y = y + 9
    print y
    print "this is not what I want imported"
