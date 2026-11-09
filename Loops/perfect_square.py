# Check whether the given number is a Perfect square>>

number=int(input("Enter a number :"))
i=2
a=0
for i in range(i,number,1):
   
    if(i*i==number):
       a="Pwefect square!"
       break            # break ka use karna important tha>>
    else:a="Not a pwerfect square!"

print(a)



