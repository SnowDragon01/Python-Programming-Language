marks={}            # Khali dictionary create kane ka tarika!

# Added keys and its values!
marks["Maths"]=96
marks["Chemistry"]=64
marks["Physics"]=35

# dict ban chuki hai >>

# loop karne ke liye hume ek key or ek value chahiye uske name kuch bhi rakhsakte ho ! and we use items() to acess its items>>
for k,v in marks.items():
    print("key :",k)
    print("Value :",v)


piyush={
    "Name":"Piyush Singh",
    "School":"G.S Public School",
    "Age":20,
    "Height":5.4,
    "FavShow":"All Of Us Are Dead!",
}    
for key,value in piyush.items():
    print("\nkey :",key,",value :",value)
    # print("\nValue :",value)