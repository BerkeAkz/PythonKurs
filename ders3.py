#random number

import random #radnom modülünün kütüphanesini dahil ettik

"""
#random.seed(7) #sistem saatinden çekilen değeri sabit olarak alıyor. tekrarlanabilir rasgelelelik 

print(random.random())


state1=random.getstate()  #mevcut saati sabitini al ve onu koru bir değişkende 

print(random.random())
random.setstate(state1) #set state ile o sabiti geri çağır set bir altındaki print için çalıştı
print(random.random())
print(random.random())


print(random.getrandbits(8)) #8 bit bazında bir sayı üret 

print(random.randrange(1,101)) #iki sayı arasında rastgele bir sayı döndürme metodu 1 dahil 101 dahil değil 
                               #bazen 3 parametre alabilir başlangıç , son(ama dahil değil), adım(atmala). 

print(random.randrange(1,11,3)) #adım mantığı 1+3 = 4 4+3=7 7+3= 10 yani 1,4,7,10 gelebilir sadece 

print(random.randint(1,10)) #hem 1 hem 10 2. parametrede dahil

 """
"""
mylist=["siyah","beyaz","turuncu","mor","mavi"]

print(random.choice(mylist)) #listeden rastgele çekti

text="berkeakgöz"
 
print(random.choice(text)) #textten rastgele bir harf getirdi

mylistManifest=["Zoktay","Hilal","Esin","Lidya","Mina","Sueda"]

print(random.choices(mylistManifest,weights=[2,2,1,2,1,3],k=18))

"""
mylistManifest=["Zoktay","Hilal","Esin","Lidya","Mina","Sueda"] 
random.shuffle(mylistManifest) #listeki elemanları rastgele sırala orijinal halini değiştirir
print(mylistManifest)          # listeyi bas
print(mylistManifest)

print(random.sample(mylistManifest,k=2)) #1.parametredeki listeden 2. parametredeki sayı kadar rastgele eleman döndürür orjinini korur


print(random.uniform(30,70)) #30-70 arasında float rastgele sayı üretir

print(random.triangular(30,70,67)) #30-70 arasında  ondalıklı sayı üretir ama 67 çevresinde olur 
