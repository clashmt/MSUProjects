gint = raw_input("What was your numerical test score?")

try:
    gint = float(gint)
except:
    print "this is not a number you dingus"
    exit()
if gint > 100:
    print "This is not a real grade you dingus"
    exit()
else:

    if gint > 1 and gint <= 100:
        gint = gint/100
        if gint <= 1 and gint >= .9:
            print "Your grade is an A"
        elif gint < .9 and gint >= .8:
            print "Your grade is an B"
        elif gint < .8 and gint >= .7:
            print "Your grade is an C"
        elif gint < .7 and gint >= .6:
            print "Your grade is an D"
        else:
            print "Your grade is an F"
    else:
        if gint <= 1 and gint >= .9:
            print "Your grade is an A"
        elif gint < .9 and gint >= .8:
            print "Your grade is an B"
        elif gint < .8 and gint >= .7:
            print "Your grade is an C"
        elif gint < .7 and gint >= .6:
            print "Your grade is an D"
        else:
            print "Your grade is an F"



