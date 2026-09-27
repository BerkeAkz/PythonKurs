#Arrayler

#listler -> sıralı , değiştirebilir , yinelenebilir
#tuple -> sıralı ,değiştirilemez ,yinelenebilir
#set -> sıralı  değil, değiştirelemez ,yinelenemez
#dictionary->sıralı,değiştirebilr, yinelemez 
meyveler=["elma","armut","erik","çilek","portakal","mandalina","şeftali"]

print(meyveler[1]) #armut

print(meyveler[-3]) #portakal sondan 3.

print("-----------------------------------------------------")

numaralar=[1,2,3,4,5] 


meyveler2=list(("elma","armut","erik","çilek","portakal","mandalina","şeftali")) #meyveler=meyveler2 

print(meyveler[2:5]) #2. indexten başla 5. indexe dahil değil
print("-----------------------------------------------------")

meyveler[1]="ayva" # değiştirebildik

print(meyveler)
print("-----------------------------------------------------")

meyveler[1:3]=["armut","muz"]


print(meyveler)
print("-----------------------------------------------------")


if "elma" in meyveler:
    print("Bu Meyve Listeini İçindedir")
else :
    print("Bu Meyve Listenin İçinde Değildir")

print("-----------------------------------------------------")
print("-----------------------------------------------------")
print("-----------------------------------------------------")
#listelere Veri Ekleme
meyveler=["elma","armut","erik","çilek","portakal","mandalina","şeftali"]+["muz","kiraz"] # +2 öğe ekledik

print(meyveler)
print(len(meyveler)) #9

print("-----------------------------------------------------")
yeniMeyvelist=meyveler+["vişne"]
print(yeniMeyvelist)
print(len(yeniMeyvelist)) #10

print("-----------------------------------------------------")
print("-----------------------------------------------------")
print("-----------------------------------------------------")

#list metodları 
meyveler=["elma","armut","erik","çilek","portakal","mandalina","şeftali"]+["muz","kiraz"]

meyveler.append("vişne") #append listenin sonuna girilen elemanı ekler
meyveler.insert(1,"limon") #insert araya dahil eder ilk parametre hangi indexin yerine 2. parametre elemanı 
print(meyveler)

meyveler2=["böğürtlen","ananas"]
meyveler.extend(meyveler2) #extend iki listeyi birleştirir içine yazılan listi sonuna ekler
print(meyveler)

print("-----------------------------------------------------")

meyveler3=meyveler.copy() #bağımsız yeni list alanı açar ve kopyalar
print(meyveler3)
print(meyveler)

meyveler4=list(meyveler) # list metoduyla birlikte yine kopyalama yapabiliriz

print("-----------------------------------------------------")
print("-----------------------------------------------------")
print("-----------------------------------------------------")

#çıkartma
meyveler.remove("şeftali") #yazılı parametredeki değeri bulur ve listten çıkarır
print(meyveler) 

cikarilan=meyveler.pop() #pop listenin sonundaki elemanı listeden kaldırır, içine index numarası vererekte listeden çıkarabiliriz
print(meyveler) 
print(cikarilan)#bize çıkarılan elemanı geri döndürür 

del meyveler[1] #meyvelere listesindeki 1. indeksi  kaldırır limon silinir 
print(meyveler)


dönenindex=meyveler.index("çilek") #çileğin indeksini döner
print(dönenindex)


meyveler.clear() #listeyi temizler 
print(meyveler)

print("-----------------------------------------------------")
print("-----------------------------------------------------")
print("-----------------------------------------------------")
meyveler=["elma","armut","erik","çilek","portakal","mandalina","şeftali"]+["muz","kiraz"]

numaralar=[9,1,7,4,5,6,8,3,2]

meyveler.sort() #stringlerde adan zye
numaralar.sort() #küçükten büyüğe

print(meyveler)
print(numaralar)

meyveler.sort(reverse=True) 
numaralar.sort(reverse=True)

print(meyveler)
print(numaralar)


