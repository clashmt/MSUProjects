def computepay(hours,rate):
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

print computepay(60,10)
