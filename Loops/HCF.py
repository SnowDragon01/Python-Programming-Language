# Find the HCF (Highest Common Factor) of two given numbers !

num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))

# num1 ke factor ka list banaya!
factorofnum1=[]
for i in range(1,num1+1,1):
    if(num1%i==0):
        factorofnum1.append(i)
# print(factorofnum1)

# num2 ke facotor ka list banaya !
factorofnum2=[]
for i in range(1,num2+1,1):
    if(num2%i==0):
        factorofnum2.append(i)
# print(factorofnum2)

# dono list me jo common hai usko common name wale list me dal diya!
common=(set(factorofnum1).intersection(factorofnum2))

hcf=max((common))
print("HCF :",hcf)
