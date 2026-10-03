#lambda fonk
#tek satırlık fonksiyonları kısaltmak için

result=lambda x: x+10

print(result(5))

sum=lambda x,y,z: x+y+z

print(sum(1,2,3))

carpma=lambda x,y:x*y
print(carpma(5,1))

kosullu=lambda x: "Pozitif" if x>0 else "Negatif"
print(kosullu(19))
print(kosullu(-19))

#bir fonksiyonu list veya tuple uygulamak için map kullanırız 

def carpma2(x):
    return x*2

numbers=[7,4,19,2]

result2=map(carpma2,numbers)  #map ilk parametre uygulanacak fonksiyon ikinci parametre list tuple set 

print(list(result2))

result3=map(lambda x: x*2,numbers)

print(list(result3))

#filter() #filtrelemek için

result4=filter(lambda x: x%2!=0,numbers)
print(list(result4))

meyveler=["elma","erik","kivi","çilek"]
result5=filter(lambda x: len(x)>5, meyveler)
print(list(result5))

print("----------------------------")
print("----------------------------")
print("----------------------------")
print("----------------------------")
print("----------------------------")

#decorator function
#hali hazırdaki fonksiyonu alıp onu geliştirip geri döndürür
#çalışmadan ya da çalıştıktan sonra bir işlem yaptırmak için

def decorator(fonk):
    def wrapperFonk(*args,**kwargs):
        print(f"Start")
        result=fonk(*args,**kwargs)
        print(f"End")
        return result
    return wrapperFonk

@decorator

def mesaj():
    print("Bu bir örnek Fonksiyondur")

mesaj()
