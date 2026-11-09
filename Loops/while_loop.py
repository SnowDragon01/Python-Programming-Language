# printing natural number upto 100..
# number=1
# while (number<=100):
#     print(number)
#     number+=1
# print("We are out of while loop!")

# we will print the sum of natural number ..
number=int(input("Enter a number :"))
i=1
sum=0
while(i<=number):
    sum=sum+i
    i+=1
print(f"The sum of natural number upto {number} is :",sum)
