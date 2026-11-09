# Find the smallest digit in the given number !
digit=input("Enter your digit :")
min=9999999999999999999999999999.  # boht badi value dalne ka logic !
for elements in range(0,len(digit)-1,1):
    
    if(int(digit[elements])<=min):
        
        min=int(digit[elements])    # type conversion ka dhyan rakhna !
        
print(min)


