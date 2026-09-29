#tuple 
#tuple sıralı ve bu sıra değimez , değiştirilmez eklenemez  çıkartılamz bir yapıdır

meyveler=("muz","armut","elma","karpuz","limon","erik") #sayı veya boolen da olabilirdi
meyve=("ayva",) #tuple olduğununn belirtmek için sonuna , koymak lazımdır yoksa string sanar 
complextuple=("Berke",21,True,"Alper",16)
print(meyveler)
print(len(meyveler))
print(complextuple)

meyveler1=tuple(("muz","armut","elma","karpuz","limon","erik")) 
meyveler2=list(meyveler1) #list'e çevirip istediğimiz ekleme çıkartma değiştirme işlemlerini yapıp sonra tekrar tuple cevirebiliriz

meyveler2[2]="çilek"

meyveler1=tuple(meyveler2) 

print(meyveler1)

meyveler+=meyve # meyveler tuple'ına meyve tuple'ı ile birleştirdik 
print(meyveler)

del meyveler

#print(meyveler)  # delete işleminden sonra yazdırmaya çalışırsak ulaşamayız

meyveler=("muz","armut","elma","karpuz","limon","erik")

for item in meyveler:
    print(item,end=" ")

for item in range(len(meyveler)):
    print(meyveler[item])

print("----------------------------------------------")
print("----------------------------------------------")
print("----------------------------------------------")

#set liste yapısı
# sıralanmamış değiştirilemez yinelemez
meyveler={"muz","armut","elma","karpuz","limon","erik","muz"}

print(meyveler)
print(len(meyveler)) #7 olmasına rağmen tekrarlı veri olduğu için 6 olur 

complexSet={"Berke",21,False,0,"Akgöz",21,True,1} #farklı veri tiplerini tutabilir
print(complexSet)

#set üyelerine erişim

#print(complexSet[0]) # hata verir 

for item in complexSet:
    print(item)

complexSet.add("çilek") #ekleme metodunu  kullanabiliriz 
complexSet.update(meyveler) #set birleştirme sonuna
complexSet.remove("muz") #discard ta kullanılabilirdi
print(complexSet)

complexSet.clear() # tüm listeyi boşalttı

setnumber={1,2,4,6,8}
setnumber2={1,4,5,3,9}

sonuc=setnumber.intersection(setnumber2)  #ortak birleşimi alır birleşim kümesi
print(sonuc)


print("----------------------------------------------")
print("----------------------------------------------")
print("----------------------------------------------")

#dictionary 
#sıralı değiştirebilir yinelenemez


araba={
    "Marka":"Hyundai",
    "Model":"i20",
    "Yıl":"2020", # tekrarlanmaz bu yüzden en son değeri kabul eder
    "Yıl":"2017",
    "Renk":["gri","beyaz","kırmızı"],
     "yakıtBenzinMi":True
}

print(araba)
print(type(araba))
print(araba["Marka"],araba["Model"])
print(len(araba)) # tekrarlanmayı saymaz 4 tanedir

anahtarlar=araba.keys()
print(anahtarlar) #anahtarları getirir

degerler=araba.values()
print(degerler)

del araba