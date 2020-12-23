
fname= str(input("Enter the first name"))
lname= str(input("Enter the last name")) 
age= int(input("Enter the age"))
dataob= int(input("Enter the date of birth"))

plist = [fname, lname, age, dataob]
for i in range(len(plist)): 
    x = plist[i]
    print(x)
if age < 18: 
    print("You can't go out because İt's too dangerous ")
else:
    print("You can go to the street")