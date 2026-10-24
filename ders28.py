#dosya oluştuma Ve Okuma işlemleri

f=open("Files/demo.txt","r",encoding="utf-8") 
# 1. parametre dosya adı 
# 2.parametre modlardır ve bu modlar şu sekilde
"""
r okuma modu varsayılan budur dosya yoksa hata verir 
t metin modunur buda varsayılandır bişi yazmassak rt şeklindedir
w yazma modudur yazma için dosya açar dosya yoksa oluşturur eğer varsa o dosya içeriğini siler üzerine yazar
a ekleme modudur eklemek için bir dosya açar dosya yoksa oluşturur

3. parametre encoding  utf-8 ile türkçe karakter  
"""

print(f.read()) 
# read metodu tüm dosyayı okur eğer sadece 10 karakter okumak isteseydik Read(10) yazmalıydık

print("-----------------------")
print("-----------------------")

f=open("Files/demo.txt","r",encoding="utf-8") 
print(f.readline()) #satır satır okur bu 1. satırı getirir
print(f.readline()) #bu 2. satırı getirir 

print("-----------------------")
print("-----------------------")

f=open("Files/demo.txt","r",encoding="utf-8") 

for line in f:
    print(line,end="")


print("-----------------------")
print("-----------------------")

f=open("Files/demo.txt","r",encoding="utf-8") 

for line in f.readlines():
    print(line,end="")


#seek metodu imleçinin yerini ayarlar 
f.seek(0)

print("-------------")
#Dosya açık mı değil mi kontrol 
print(f.closed)# FAlse


f.close() #Dosyayı kapatır 

print(f.closed) #true
#with ile kullanım

with open("Files/demo.txt",encoding="utf-8") as f: #önceden open yapar  sonra close yapmak gerekirdi with ile close yapmaya gerek yok 
    print(f.read(10))
    print(f.tell()) #imlecin nerde olduğu verir anlık
    print(f.read(10))
    print(f.tell())
print("-----------------")

with open("Files/demo.txt",encoding="utf-8") as f:
    for line in f:
        print(line,end="")


print("-----------------")

with open("Files/demo.txt","r",encoding="utf-8") as f:
    print(f.readable()) #dosyam okulanabilir modda mı True

print("-----------------")

with open("Files/demo.txt","w",encoding="utf-8") as f:
    f.write("How is it going\n") #önceki içeriği siler ve yazılanı yazar 

with open("Files/demo.txt","r",encoding="utf-8") as f:
    print(f.read())


print("-----------------")
with open("Files/demo.txt","a",encoding="utf-8") as f:
    f.write("Öncekinin üzerine Eklenecek\n") 

with open("Files/demo.txt","r",encoding="utf-8") as f:
    print(f.read())

print("-----------------")

with open("Files/demo.txt","w+",encoding="utf-8") as f: # hem yaazılabilir hemde okunabilir dosya açtık aynı with altında hem yazdık hem okuduk
    f.write("Yeni Dosya")                               # ekleme yapmak istersek onun yerine a+ yapmamız lazım
    f.seek(0)
    print(f.read())

with open("Files/demo.txt","r+",encoding="utf-8") as f: # bunda da hem okuma hem yazma işlemini yapar 
    f.write("Yeni Dosya")                               #w+ siler bu silmeden ekleme işleminide yapar hem okur hem yazar
    f.seek(0)
    print(f.read())
    