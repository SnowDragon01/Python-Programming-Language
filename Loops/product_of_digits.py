# Find and print the product of all digits of a given number.

number=input("Enter a number :")
i=0
product=1
for i in range(i,len(number),1):
    product=product*int(number[i])
print("product of all the digits is :",product)