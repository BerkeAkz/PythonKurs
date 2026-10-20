#Regular Expression RegEX

import re 

text="The rain in Türkiye"

result=re.search("^The.*Türkiye$",text) # seach metodu ara The ile Başlaycak Türkiye ile Bitecek 
if result:
    print("Yes! we have a match!")
else:
    print("No match")

print(result) 

print("----------------------------------")
# örneğin kullanıcıdan Telefon numarası girmesini istedik ve kullanıcı numara yerine string ifade girmiş olabilir veya sayısını fazla girmiş olabilir
#böyle durumları kontrol eder 

text="Hello Python 3. Regular expression is awesome "

result=re.findall("Python",text) # findall içinde var mı diye bakar
if result:
    print("Yes! we have a match!")
else:
    print("No match")

print(result) 

print("----------------------------------")

text="Hello Python 3. Regular expression is awesome "

result=re.findall(r"[a-f]",text) # [] koşul a-f arasındaki a-f dahil harfler geçiyor mu diye bakar list döndürür
if result:
    print("Yes! we have a match!")
else:
    print("No match")

print(result) 

print("----------------------------------")

text="Hello Python 3. Regular expression is awesome "

result=re.findall(r"\d",text) # [] k  #r rowstring \d kaçış karakteri algılama 
if result:
    print("Yes! we have a match!")
else:
    print("No match")

print(result) 

print("----------------------------------")

text="Hello Python 3. Regular expression is awesome "

result=re.findall(r"P....n",text) #p ile başlayan n ile biten kelimeleri getir 
if result:
    print("Yes! we have a match!")
else:
    print("No match")

print(result) 


print("----------------------------------")

text="Hello Python 3. Regular expression is awesome "

result=re.findall(r"^H",text) #Text H ile mi başlar 
if result:
    print("Yes! we have a match!")
else:
    print("No match")

print(result) 
print("----------------------------------")

text="Hello Python 3. Regular expression is awesome "

result=re.findall(r"awesome$",text) #Text awesome ile mi biter
if result:
    print("Yes! we have a match!")
else:
    print("No match")

print(result) 

print("----------------------------------")

text="ı am 21 years old  "

result=re.findall(r"\d{1,3}",text) #yaş en az 1 en fazla 3 rakam olabilir 
if result:
    print("Yes! we have a match!")
else:
    print("No match")

print(result) 

print("-----------------------------")
print("-----------------------------")

#uygulama 

import re

def is_valid_email(email):
    pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]\.[a-zA-Z]"
    return re.fullmatch(pattern,email)     
     

while True:
    name=input("Enter your Name:")
    if re.fullmatch(r"[a-zA-Z]+",name): #Sadece büyük küçük harf
        print(f"Thanks Your name is {name}")
        break
    else:
        print("are you stupid?")

    yas=input("Enter your age:")
    if re.fullmatch(r"\d+",yas): #Sadece sayı
            print(f"Thanks Your age is {yas}")
            break
    else:
         print("are you stupid?")

    email=input("Enter your email")
    if is_valid_email(email):
        print("doğru email")
        break
    else:
        print("Yanlış email")





