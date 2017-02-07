def computepay():

    hours = raw_input("How many hours did you work this week?")
    try:
        hours = float(hours)
    except:
        print "Not a number you dingus"
        exit()
    rate = raw_input("What is your hourly rate?")
    try:
        rate = float(rate)
    except:
        print "Not a number you dingus"
        exit()
    text = "Pay: "

    if hours > 40:
        ot = (hours % 40) * (1.5 * rate)
        otpay = (40 * rate) + ot
        otpay = str(otpay)
        print text + otpay
    if hours <= 40:
        pay = rate * hours
        pay = str(pay)
        print text + pay


print computepay()





