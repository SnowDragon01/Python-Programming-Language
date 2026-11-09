# agar list int/float ka bna hua hai to
# we can use max() and min() to get the maximum and minimum value..
# tuple is a list that isnt mutable jise change nahikiya ja sakta..
percentage=(56.2,35.02,90,89.44,87.4,99.9,92.77);

print("Maximum percentage :",max(percentage)) # maximum percentage..
print("Minimum percentage :",min(percentage)) #minimum percentage ..

# we use len() to get kitne datas stored hai wo janne ke liye..
print("length of list :",len(percentage)) #zaruri nhi ki list sirf number ka hi rhe..

friend=("Himanshu",18,"Paneer Patties") #tuple ban gya..
print(friend[0:])
# indexing is also possible..

# creating empty tuple..
student=()
#creating a tuple of size one ..
student=(1,) # comma is imp ye nhi rrhega toh computer ise int consider karega..

#hum do tuples ko add bhi kar sakte haiin
tup1=("Himanshu",18,"Paneer Patties")
tup2=(56.2,35.02,90,89.44,87.4,99.9,92.77)

print(tup1+tup2)

# we cannot directly add or remove elements in tuple but we cant do such thing by tycasting tuple in to list and again convert it into tuple

# we can also know that the number of occurance of a particular item in the tuple>> by using .count("string")
