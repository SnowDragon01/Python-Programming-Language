# we will create a list of squares of number from 1 to 10 !

squares=[]
square=0
for num in range(1,11):
    # square=num*num
    squares.append(num**2)  # direct kar diya !
print(squares)

print("Max :",max(squares))
print("Min :",min(squares))
print("Sum :",sum(squares))


