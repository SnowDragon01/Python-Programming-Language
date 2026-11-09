# Find and print the sum of digits of the given number>>

digit=input("Enter a digit :")
i=0
sum=0
for i in range(i,len(digit),1):
    sum=sum+int(digit[i])
print("Sum of the digit is :",sum)