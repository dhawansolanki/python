def sum_of_even(n):
    total = 0
    for i in range(1, n+1):
        even_number=2*i
        total=total+even_number
    return total
n = int(input("Enter n : "))
result= sum_of_even(n)
print ("Sum of all even numbers from 1 to", n,"is: ",result)