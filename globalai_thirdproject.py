import random

human = input("Please enter your name") 
print("Welcome to the game" , human) 
word = ["araba", "traktör" , "motorsiklet" , "bisiklet" , "jip" , "suv"]  
new =list(random.choice(word))
ek = [" "] * len(new) 
claim = 7 
fnl  = 0 
snc = False 

while claim!=0: 
    chosen=input("Game has started. Please enter word")
    for i in new: 
        fnl+=1 
        if i==chosen: 
            snc=True
            ek[fnl - 1 ]=chosen 
        if " " not in ek: 
            print("Congratulations" , human)
            cevap = input("do you want to log out?  ['e' veya 'h'] :")
            if cevap == "e":
                print("you logged out") 
                exit()
    if snc==False: 
        claim-=1 
        print("You guessed wrong") 
        print(claim, "you have left right", human)

    if claim==0 and " " in ek: 
        print("You lost the game", human) 
        cevap = input("do you want to log out?  ['e' veya 'h'] :")
        if cevap == "e":
                print("you logged out")        
        if cevap == "h":
            tahmin = input("Kelimenin tamamını yahmin edebilirsiniz. Bir hakkınız var")
            if tahmin == new: 
                print("Tebrikler bildiniz")
                break
            else: 
                print("Bilemediniz ve kaybettiniz")
                break

         
    
    fnl=0
    snc=False
    print(ek)
    
