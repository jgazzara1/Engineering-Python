age = 19
interest1 = "football"
interest2 = "python"
#150 data points

if age > 18 and interest1 == "football":
    def showVideos():
        print "Show mature content"
        print "Show clips related to football"
        print "Show clips related to sports, in general"
elif age < 18 and interest1 == "cooking":
    def showVideos():
        print "No mature content"
        print "Show new recipes"
else:
    def showVideos():
        print "Show default video recommendations"

showVideos()
