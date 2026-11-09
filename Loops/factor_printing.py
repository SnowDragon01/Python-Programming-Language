# Print all factors of the given number !
number=int(input("Enter a number :"))
for element in range(1,number+1,1):
    if(number%element==0):
        print(element)