marks_phy=int(input("Enter your marksk in physics :"))
marks_chem=int(input("Enter your marksk in chemistry :"))
marks_maths=int(input("Enter your marksk in maths :"))

marks=[]

marks.append(marks_phy)
marks.append(marks_chem)
marks.append(marks_maths)

total=sum(marks)
percentage=(marks[0]+marks[1]+marks[2])/3
print("\tTotal :",total)
print("\tpercent: ",round(percentage,2))

if percentage>=90:
    print("Grade :A")
elif percentage>=80 and percentage<90:
    print("Grade :B")
elif percentage>=70 and percentage<80:
    print("Grade :C")
elif percentage>=50 and percentage<70:
    print("\tGrade :D")
elif percentage<50:
    print("Grade :F")
