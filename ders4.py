print("hello")
print('hello') #aynı çıktı verir

text="""Bu bir çoklu satır
textidir 
"""

print(text)

mylistManifest=["Zoktay","Hilal","Esin","Lidya","Mina","Sueda"]

print(mylistManifest[0])

text2="BerkeAkz" #stringler bir arraydir 

print(text2[5]) 

print(len(text2)) #dizinin uzunluğu

text3="En iyi diller bedava öğrenebildiğin dillerdir "

print("bedava" in text3) # in içinde var mı diye kontrol boolen true döner
print("pahalı" in text3) #boolen false döner

search="kötü"

if search in text3: #in var mı 
    print(search + " kelimesi textin içinde")

if search not in text3: #not in yok mu 
    print(search + " kelimesi textin içinde değil  ")   



#dilimleme

text4="python güzeldir"

print(text4[1:5]) #ytho 1 dahil 5 değildir
print(text4[:5]) #pytho ilkini varsayılan 0 alır bişi yazmayınca
print(text4[5:]) # sonuna kadar gider 
print(text4[-5:-1]) #tersten dilimleme bu ssefer 1. par. dahil değil 2. dahil

#birleştirme

text5="Berke"
text6="Akgöz"

print(text5+text6) #BerkeAkgöz
print(text5,text6) #Berke Akgöz


print(text5.upper()) #harfleri büyük yaptı
print(text5.lower()) #harfleri  küçük yaptı

text7=" kenarlarda bir boşluk var "
print(text7.strip()) #yanlardaki fazladan boşlukları kaldıracak 

print(text7.split( ))

