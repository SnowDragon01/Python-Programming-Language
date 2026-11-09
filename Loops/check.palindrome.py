# Check whether the given number is a palindrome>>

digit=input("Enter odd numbered digit :")
i=0
j=len(digit)-1
digits_are=0
for i in range(i,len(digit),1):
    if(digit[i]==digit[len(digit)-1-i]):
        digits_are="Palindrome!"
    else: digits_are="Not a Palindrome!"
    
print(digits_are)