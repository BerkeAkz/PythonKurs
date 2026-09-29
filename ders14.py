#koşullu ifadeler


a=int(input("Bir Sayı Gir:"))
b=int(input("Bir Sayı Daha Gir:"))

if(a>b):
    print(f"İlk Girdiğin Sayı {a} Daha Büyüktür {b} den")
elif(b>a):
    print(f"İkinci Girdiğin Sayı {b} Daha Büyüktür {a} den")
else:
    print("Bu Sayılar Eşit")



x=int(input("Bir Sayı Girin:"))

if(x>0):
    print(f"{x} Pozitiftir")
    if(x>10):
         print("pozitif ve 10dan büyük")
    else:
         print("pozitif ve 10dan küçük")
elif(x<0):
     print(f"{x} negatiftir")
else:
      print(f"{x} = 0")



#uygulama 1

vize=float(input("Vize Notunu Gir:"))
final=float(input("Final notunu Gir:"))

ortalama=float((vize*0.4)+(final*0.6))

if(ortalama>=90):
    print(f"Ders Dönem Ortalaması: {ortalama} Ve Harf Notu: AA")
elif(ortalama>=80):
    print(f"Ders Dönem Ortalaması: {ortalama} Ve Harf Notu: BA")
elif(ortalama>=70):
    print(f"Ders Dönem Ortalaması: {ortalama} Ve Harf Notu: BB")
elif(ortalama>=60):
    print(f"Ders Dönem Ortalaması: {ortalama} Ve Harf Notu: BC")
elif(ortalama>=50):
    print(f"Ders Dönem Ortalaması: {ortalama} Ve Harf Notu: CC")
else:
    print(f"Ders Dönem Ortalaması: {ortalama} Ve Harf Notu: FF")


#uygulama2

harf=input("Lütfen Bir Harf Girin:")

if(len(harf) != 1):
    print("Lütfen karakter Girin")
else:
    if(harf.isalpha()):
        print("Bu Bir Harftır")
        
        if(harf.isupper()):
            print("Büyük Harf Girilmiştir")
        else:
            print("Küçük Harf Girilmiştir")

        sesliHarfler="AEIOUaeiou"
        if(harf in sesliHarfler):
           print("Sesli Harftir")
        else:
           print("Sessiz Harftir")
    else:
        print("Lütfen Geçerli Bir Harf Girin")



