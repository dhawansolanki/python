l = []
n = int(input("Enter the size : "))
for i in range(n):
    num = int(input("Enter element at %d position"%(i)))
    l.append(num)
t1 = tuple(l)
print("The elements in the tuple are : ",t1)
print("The elements in the tuple after sorting are : ",sorted(t1))
print("The Maximum element in the tuple are : ",max(t1))
print("The Minimum element in the tuple are : ",min(t1))
if t1 == tuple(l):
    print("All the elements are equal")
else:
    print("Not all the elements are equal")