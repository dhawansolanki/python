def histogram(lst):
    print("The Histogram for the list is : ")
    for i in range(len(lst)):
        for j in range(lst[i]):
            print('-', end=' ')
        print(' ')
lst = []
n = int(input("Enter the size of the list : "))
for i in range(n):
    ni = int(input("Enter the psoition at %d position"%(i)))
    lst.append(ni)
histogram(lst)