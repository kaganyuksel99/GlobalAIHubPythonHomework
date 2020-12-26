ad = "kağan"
soyad = "yüksel"

derslistesi = ["algoritma" , "matematik" , "türkçe" , "fizik" , "kimya"]

vize = 0 
final = 0 
project = 0 
x= 1

adgirisi = str(input("Sisteme giriş için adınızı girer misiniz"))
soyadgiris = str(input("Sisteme giriş için soyadınızı girir misiniz"))

while x <=4: 
    if x==4: 
        print("Fazla giriş denemesi yaptınız. Lütfen daha sonra tekrar deneyiniz")
        break
    if (ad != adgirisi or soyad !=soyadgiris):
        print("Adınızı ya da soyadınızı hatalı girdiniz")
        adgirisi = str(input("Sisteme giriş için adınızı girer misiniz"))
        soyadgiris = str(input("Sisteme giriş için soyadınızı girir misiniz")) 
        i +=1
        continue
    else: 
        print("WELCOME!" , ad) 
        print(f'{derslistesi[0]} , {derslistesi[1]} , {derslistesi[2]} , {derslistesi[3]} , {derslistesi[4]} derslerini alabilirsiniz')
        kacders = int(input("Kaç adet ders girdiniz")) 

        if 3 <= kacders <=5: 
            dersbelirt = input("Lütfen aldığınız derslerden birinin adını giriniz")
            if dersbelirt == "algoritma": 
                algoritma_not = {vize: 55 , final: 61 , project: 80}
                hesaplama= algoritma_not[vize]*0.3 + algoritma_not[final]*0.5 + algoritma_not[project]*0.2 
                if hesaplama >= 90: 
                    print("Harika, Harf notunuz AA")
                elif 70 <= hesaplama <90: 
                    print("Güzel, Harf notunu BB") 
                elif 50 <= hesaplama <70:
                    break
                    print("Orta, Harf notunu CC")
                elif 30 <= hesaplama <50: 
                    print("Kötünün iyisi, Harf notunu DD")  
                else: 
                    print("Dersten kaldınız, Harf notunuz FF")
        
            if dersbelirt == "matematik": 
                matematik_not = {vize: 85 , final: 75 , project: 60}
                hesaplama= matematik_not[vize]*0.3 + matematik_not[final]*0.5 + matematik_not[project]*0.2 
                if hesaplama >= 90: 
                    print("Harika, Harf notunuz AA")
                elif 70 <= hesaplama <90: 
                    print("Güzel, Harf notunu BB") 
                elif 50 <= hesaplama <70:
                    print("Orta, Harf notunu CC")
                elif 30 <= hesaplama <50: 
                    print("Kötünün iyisi, Harf notunu DD")  
                else: 
                    print("Dersten kaldınız, Harf notunuz FF")
        
            if dersbelirt == "türkçe": 
                turkce_not = {vize: 74 , final: 59 , project: 100}
                hesaplama= turkce_not[vize]*0.3 + turkce_not[final]*0.5 + turkce_not[project]*0.2 
                if hesaplama >= 90: 
                    print("Harika, Harf notunuz AA")
                elif 70 <= hesaplama <90: 
                    print("Güzel, Harf notunu BB") 
                elif 50 <= hesaplama <70:
                    print("Orta, Harf notunu CC")
                elif 30 <= hesaplama <50: 
                    print("Kötünün iyisi, Harf notunu DD")  
                else: 
                    print("Dersten kaldınız, Harf notunuz FF")
            
            if dersbelirt == "fizik": 
                fizik_not = {vize: 22 , final: 39 , project: 70}
                hesaplama= fizik_not[vize]*0.3 + fizik_not[final]*0.5 + fizik_not[project]*0.2 
                if hesaplama >= 90: 
                    print("Harika, Harf notunuz AA")
                elif 70 <= hesaplama <90: 
                    print("Güzel, Harf notunu BB") 
                elif 50 <= hesaplama <70:
                    print("Orta, Harf notunu CC")
                elif 30 <= hesaplama <50: 
                    print("Kötünün iyisi, Harf notunu DD")  
                else: 
                    print("Dersten kaldınız, Harf notunuz FF")
            
            if dersbelirt == "kimya": 
                kimya_not = {vize: 22 , final: 39 , project: 70}
                hesaplama= kimya_not[vize]*0.3 + kimya_not[final]*0.5 + kimya_not[project]*0.2 
                if hesaplama >= 90: 
                    print("Harika, Harf notunuz AA")
                    
                elif 70 <= hesaplama <90: 
                    print("Güzel, Harf notunu BB") 
                elif 50 <= hesaplama <70:
                    print("Orta, Harf notunu CC")
                elif 30 <= hesaplama <50: 
                    print("Kötünün iyisi, Harf notunu DD")  
                else: 
                    print("Dersten kaldınız, Harf notunuz FF")
            
            
            






