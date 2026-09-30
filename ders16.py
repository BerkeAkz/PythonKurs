#Fonksiyonlar

def cikti():
    print("------")

cikti() # çağırmassak çalışmaz

def isim(ad):  #parametreli fonksiyon 
    print(f"İsim={ad}")

isim("Berke")

def tamisim(ad,soyad):
    print(f"İsim={ad} Soyisim={soyad}")

tamisim("Berke","Akgöz")


def name(**par):
    print("Soyadı="+par["lastname"])

name(firstname="Berke",lastname="Akgöz")

def my_country(country="Türkiye"):
    print("Benim Ülkem="+country)

my_country() #default değer gelir
my_country("İtaly") # girilen parametre gelir

def meyvelerFonk(meyve):  
    for item in meyve:
        print(item)

meyveler=["elma","armut","erik","çilek","portakal","mandalina","şeftali"]
meyvelerFonk(meyveler)


def carp(x):
    return x*7

print(carp(5)) #sonucu print ile yazdırmak
sonuc=carp(7)
print(sonuc) #yada değişeken atayıp 

def passfonk():
    pass  #veya ...

def myfonk(x,/):
    print(x)

myfonk(7) #içine x=7 yazılamaz 


def myfonk2(*,x):
    print(x)

myfonk2(x=7) #içine yalnızca 7 yazsa hata alır

def hello():
    print("hello")

for item in range(7):
    hello()


def controlReturn(number): #tek return olmadığını gösteren uygulama
    if(number>0):
        return "pozitif"
    elif(number<0):
        return "negatif"
    else:
        return "Sıfır"

print(controlReturn(7))


def multiply(number):
    return number*7

def myFonk(fonkAd,deger):
    return fonkAd(deger)

result=myFonk(multiply,10)
print(result)

#recursion yinelemeli fonksiyonlar 

def fak(n):
    if(n==0 or n==1):
        return 1
    else :
        return n * fak(n-1)

print(fak(1))

#uygulama-1 

sayi=int(input("Pozitif Tam Sayılarını bulmak istediğin Sayıyı Girim:"))

sayac=sayi
sonuc=0
sonuclistesi=[]
if(sayi>0):
    while(sayac>0):
        if(sayi%sayac==0): 
            sonuclistesi.append(sayac)
            sayac-=1
        else:
            sayac-=1
    print(sonuclistesi)
elif(sayi<0):
    print("Pozitif Bir Sayı Girin")
else:
    print("Sayı sıfırfır")

 