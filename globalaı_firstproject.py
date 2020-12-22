name = list(input("what is your name?"))
surname = str(input("what is your surname")) 
study = bool(input("Do you work?")) 
age= int(input("How old are you?"))
weight = float(input("What is your weight?")) 

result = f"name {name} , surname {surname} , study {study} , age {age} , weight {weight}" 

first= type(name)
second= type(surname)
third= type(study)
fourth= type(age)
fifth= type(weight)

result = f"name {name} , surname {surname} , study {study} , age {age} , weight {weight}" 
sresult = f"name type {first}, surname type {second}, study type {third}, age type {fourth}, weight type {fifth}"
print(result)
print(sresult)