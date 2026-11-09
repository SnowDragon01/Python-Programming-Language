# Calculate and print the factorial of a given number>>

n=int(input("Enter a number :"))
i=1
factorial=1
for i in range(i,n+1,1):
    factorial=factorial*i
print(f"{n}! is :",factorial)