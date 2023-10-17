m1 = int(input("Enter Marks in Subject 1 : "))
m2 = int(input("Enter Marks in Subject 2 : "))
m3 = int(input("Enter Marks in Subject 3 : "))
total = m1+m2+m3
per=(total/300)*100
print("The total marks obtained is : ",total)
print("The total percentage obtained is : ",per)
if(per>=75):
    print("First Class with Distinction")
elif(per>=60 and per<75):
    print("First Class")
elif(per>=45 and per<60):
    print("Second Class")
elif(per>=40 and per<45):
    print("Pass")
else:
    print("Fail")