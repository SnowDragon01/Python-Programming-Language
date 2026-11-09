# check a number whether it is a prime or not !
number = int(input("Enter a number: "))

# Agar number 1 ya usse chota hai, to wo prime nahi hota
if number <= 1:
    number_is = "Number is not prime!"
else:
    number_is = "Number is prime!" 
    
    for i in range(2, number):
        if number % i == 0:
            number_is = "Number is not prime!"
            break  # Ek bhi factor milte hi loop se bahar nikal jao

print(number_is)
