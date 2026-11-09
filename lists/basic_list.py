# list is a kind of a string jo sare datatype ko store kar sakta hai..

classmate=["Sibtain Raza!",22,"Chicken Biryani"];
# ek string jaisa kuch ban gya jise mai indexing se acess kar sakta hoon..

print("Name :",classmate[0]);
print("Age :",classmate[1]);
print("Fav.food :",classmate[2]);

print(classmate); # acessing whole list..

#print(classmate[0:1]); # slicing of list..

print("__"*10); # ye bas seperate karne ka line create karta hai..

# Here we can modify elements in list which isnt possible in string ..

classmate[1]=23; # updated an element of list..

print("Name :",classmate[0]);
print("Age :",classmate[1]);
print("Fav.food :",classmate[2]);



