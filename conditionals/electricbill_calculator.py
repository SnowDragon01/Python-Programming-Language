unit=int(input("Enter unit of electricity consumed :"))
if(unit<=100):
    print("Your electric bill is :",unit*4)
elif(unit>100 and unit<=200):
    print("Your electric bill is :",100*4+(unit-100)*6)
elif(unit>200):
    print("Your electric bill is :",100*4+100*6+(unit-200)*8)