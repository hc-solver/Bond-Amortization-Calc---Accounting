#Bond Amortization
par = int(input("enter par value of bond:"))
coupon_rate = float(input("enter coupon rate:"))
Life = int(input("enter maturity periods:"))
mr = float(input("enter market rate:")) 
n = 0
cp = float(par*coupon_rate)
m = Life
x = 0
c = 0 #PV of the discount payment  
PV_Par = par/(1+mr)
Yr = int(input("At the end of which Year:"))
if Yr > Life:
    print ("Error: The year you entered is over maturity period:"+str(Life))
    Yr = input(input("Please re-enter:"))
    while n in range(m-Yr+1):     #tocalculate the PV of the interest payment 
        cp = cp/(1+mr)
        PV_Par = PV_Par/(1+mr)  #to calculate the PV of the Par value
        x = x + cp
        n += 1
    PV_Par = PV_Par*(1+mr)
    Lol = PV_Par + x
    print ("Current Value of the last period:"+str(Lol))
    print ("Interest Expense:"+str(Lol*mr))
    print ("Coupon Paid:"+str(par*coupon_rate))
    print ("Premium Amortization:"+str(Lol*mr-par*coupon_rate))
    
else:
    while n in range(m-Yr+1):     #tocalculate the PV of the interest payment 
        cp = cp/(1+mr)
        PV_Par = PV_Par/(1+mr)  #to calculate the PV of the Par value
        x = x + cp
        n += 1
PV_Par = PV_Par*(1+mr)
Lol = PV_Par + x
print ("Current Value of the last period:"+str(Lol))
print ("Interest Expense:"+str(Lol*mr))
print ("Coupon Paid:"+str(par*coupon_rate))
print ("Premium Amortization:"+str(Lol*mr-par*coupon_rate))


    
    
    
    
    
