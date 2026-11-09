a=int(input("Enter first side :"))
b=int(input("Enter second side :"))
c=int(input("Enter third side :"))

if(a==b and b==c):
    print("You have equilateral triangle!")
elif(a==b or b==c or c==a):
    print("You have isoscales triangle!")
else: print("You have scalen triangle!")
