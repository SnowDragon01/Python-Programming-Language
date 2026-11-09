# Calculate the sum of all even numbers from 1 up to n>>

n=int(input("Enter an even number :"))
i=2
sum=0
for i in range(i,n+1,2):
    sum=sum+i
print(f"sum of even upto {n} is :",sum)

