# username=['admin','piyush','umrah','sibtain','sunny']
username=[]

if username:
    for user in username:
        if user=='admin':
            print("Hello Admin Would You like to see a status report?")
        else: print("\tHello "+user+" Thankyou for logging in again!")
else: print("We need to find a user!")

