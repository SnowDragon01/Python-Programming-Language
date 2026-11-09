# we will creaate a function of nCr!

def factorial(a):
    product=1
    for i in range(1,a+1,1):
        product*=i
    return product      # Yeh value wapas bhej raha hai

def nCr(n,r):
    NCr= factorial(n)/(factorial(r)*factorial(n-r))
    print(f"{n}C{r}:",(NCr))    # ye value print kra rha hai !

nCr(7,2)








    


