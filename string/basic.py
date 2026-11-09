# name=(input("Enter your name :"));  #declaration + concatenation

# print("Your name is :",name);

# # we can use len() function to acess the length of the string..

# print("Your name has",len(name),"letters!!");

first_name="ada"
last_name="lovelace"
message=first_name.title() +" "+ last_name.title()  #concatenation!

print("Hello,"+message+"!")
print(f"Your name has {len(first_name+last_name)} letters")


# we can remove white spaces using .lstrip()/.rstrip()/.strip()
word="  python."
print(word.lstrip())    #removed left whitespace
word="python. "
print(word.rstrip())     #removed right whitespace
word="  python.  "
print(word.strip())     #removed all whitespace


