a=int(input("Enter A:"))
b=int(input("Enter B:"))
c=int(input("Enter C:"))
d=int(input("Enter D:"))

if(a>b and a>c and a>d):
    print(f"{a} is greaterst among [{a},{b},{c},{d}]!!")
elif (b>a and b>c and b>d):
    print(f"{b} is greaterst among [{a},{b},{c},{d}]!!")  
elif(c>a and c>b and c>d):
    print(f"{c} is greaterst among [{a},{b},{c},{d}]!!")
else:print(f"{d} is greatest among [{a},{b},{c},{d}]!!")    