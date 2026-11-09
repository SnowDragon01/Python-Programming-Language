# Find and print the sum of all factors of the given number !

number=int(input("Enter a number :"))
sum=0
for element in range(1,number+1,1):
    if(number%element==0):
        sum=sum+element
print(" of all the factor is :",sum)