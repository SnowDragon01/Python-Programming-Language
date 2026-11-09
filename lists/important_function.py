# agar list int/float ka bna hua hai to
# we can use max() and min() to get the maximum and minimum value..

percentage=[56.2,35.02,90,89.44,87.4,99.9,92.77]

print("Maximum percentage :",max(percentage)) # maximum percentage..
print("Minimum percentage :",min(percentage)) #minimum percentage ..

# we use len() to get kitne datas stored hai wo janne ke liye..
print("length of list :",len(percentage)) #zaruri nhi ki list sirf number ka hi rhe..

# we use .sort() to get the elements of the list in ascending order ..
percentage.sort()
print(percentage);

# we use .append(element) to add element at the end..
percentage.append(99.92);
print(percentage);

# we use .remove(element) to remove the first occurance of that element..
percentage.remove(percentage[3]);
print(percentage);

# we use .pop(i) to remove element at index i
# we use .reverse() to reverse the list ..