a=[]
n=int(input("Enter number of elements : "))
for i in range(0,n):
    t = int(input("Enter Element : "))
    a.append(t)
sum = 0
for element in a:
    sum = sum + element
print("The Sum is : ",sum)