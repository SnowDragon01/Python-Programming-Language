piyush={
    "Name":"Piyush Singh",
    "School":"G.S Public School",
    "Age":20,
    "Height":5.4,
    "FavShow":"All Of Us Are Dead!",
}                           #declared and initialised  

# we can acess the elements by using its key..
print(piyush["Name"])

# we can also acess whole dictionary..
print(piyush)

# we can update keys by a new value..
piyush["FavShow"]="Alice in borderland!"
print(piyush)

# we can also add a new key to our local dictionary..
piyush["Hobby"]="Playing Chess!"
print(piyush)

# how do i know it is a dictionary..
print(type(piyush))     #<class 'dict'>

# we can remove a key by using del list[key]
del piyush["Age"]
print(piyush)
