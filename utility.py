num = int(input("Enter a number : "))    
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("The factorial of",num,"is",factorial)   




import math  
def compound_interest(p,r,t):   
    amt = p * (math.pow((1 + (r/100)),t))
    print("Compound Amount: ",amt)
    CI = amt - p
    return CI

p=float(input("Enter Principal Amount: "))
r=float(input("Enter Rate of Interest: "))
t=float(input("Enter Time Period in years: "))

print("Compound interest is",compound_interest(p,r,t))




def simpleInterest(P, Y, R):
    SI = (P * Y * R)/100
    return SI
   
  
P = float(input("Enter the principal amount : "))
 
Y = float(input("Enter the number of years : "))
 
R = float(input("Enter the rate of interest : "))
 
#calculate simple interest by using this formula
SI = simpleInterest(P, Y, R)
print("Simple interest : {}".format(SI))