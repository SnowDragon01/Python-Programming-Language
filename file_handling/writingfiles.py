# we will try to write and read a file here >>
# writing this input in the file >>
text=input("Enter your text :")
# opening file to write/append..
f=open("/Users/harshraj/python/file_handling/demoreadfiles.txt","a")
f.write(text)
# opening file to read..
f=open("/Users/harshraj/python/file_handling/demoreadfiles.txt","r")
print(f.read())




