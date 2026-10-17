#try 

try: #deneme sınama
    print(x)
except: #hata olursa bura yakalara ve bu bloğun içi çalışır
    print("Bir hata meydana geldi")



try: #deneme sınama
    print(x)
except NameError: #eğer hata nameerror ise bunu yap
    print("Burada bir nameerror hatası meydana geldi")
except:
    print("naneerrordan farklı bir hata meydana geldi")


try: 
    x=7
    print(x)
except:
    print("Bir hata meydana geldi")
else: #herhangi gibi bir hata oluşmadığından çalışır 
    print("Herhangi gibi bir hata yoktur")


try: 
    x=7
    print(x)
except:
    print("Bir hata meydana geldi")
finally: #hata olsun  veya olmasın çalışır  
    print("try-except komutu bitti")



def age_check(age):
    if(age<0):
        raise ValueError("yaş 0dan küçük olmamalı") #kendi hata sistemimizi oluştururuz
    else:
        print(f"Age:{age}")


try:
    age_check(-7)
except ValueError as e:
    print("Error:",e)

#istisnalar 

x=7

try:
    if not type(x) is int:
        raise TypeError("Tür hatası bu sayı int değil")
    else:
        print(x)
except TypeError as e:
    print("Error:",e)


try:
    sayi=int(input("Bir Sayı gir"))
    result=10/sayi
    print("Sonuc:",result)

except ZeroDivisionError:
    print("Sayı Sıfıra Bölünemez")
except ValueError:
     print("int bir Sayı gir ")

# except AritmeticError tüm matematiksel hatalar 
# except OwerflowError taşma hatalarında 
# except Exception tüm haataları yakalar

try:
    person={"name":"fehmi",
            "age": 21}
    print(person["addres"])
except KeyError:
    print("Error:Key bulunamadı")

#LookupError, keyerror ve indexerror üst sınıfıdır  