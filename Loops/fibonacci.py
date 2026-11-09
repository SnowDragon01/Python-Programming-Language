# Print the Fibonacci series up to n terms!
n=int(input("Enter a number :"))
i=0
j=1
next_number=0
for element in range(0,n,1):
    print(next_number)
    i=j
    j=next_number
    next_number=j+i
