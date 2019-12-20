def computepay(h,r):
	if h<=40:
		sum=(h*r)
	else:
		sum=(40*r+((h-40)*1.5*r))
	return sum
hrs=input("Enter Hours:")
hrs=float(hrs)
rate=input("Enter pay:")
rate=float(rate)
p=computepay(hrs,rate)
print ("Pay",p)