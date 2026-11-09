# Print all numbers between a and b that are divisible by 7!

a=int(input("Enter a :"))
b=int(input("Enter b :"))
divident=0
for elements in range(a,b+1,1):
    if(elements%7==0):
       print(elements) 

        
        