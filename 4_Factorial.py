#Factorial without recursion : 
x = int(input("Enter the number for which you want factorial : "))
fact = 1
while(x>0):
    fact = fact * x
    x=x-1
print ("The Factorial of",x,"is: ",fact)

#Factorial with recursion : 
def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
n = int(input("Enter the number for which you want factorial : "))
r = fact(n)
print("Factorial is : ",r)