yas=21
isim="Berke"

text="Benim adım {} , Yaşım {}" .format(isim,yas)
print(text)

text=f"Benim adım {isim}, Yaşım {yas}" #f string
print(text) 

text1="bu test amacıyla yazılmış BİR texttir"

print(text1.capitalize()) # bu daki  B büyük yapar ilk harfi büyük yapar

print(text1.title()) # her kelimenin ,lk harfını büyük harfe çevirir

print(text1.swapcase()) #büyüğü küçük küçüğü büyük

print(text1.center(20,"-")) #sağdan soldan 20 birimlik ortala

text2="Welcome to  my world , My world is python"

print(text2.count("world",0,50)) #kelimenin metin içindeki sayısı 1. aranan kelime 2. başlangıç indexi 3. bitiş indexi

print(text2.startswith("Welcome")) # yazılan kelime ile mi Başlar bool true
print(text2.startswith("to")) #false

print(text2.endswith("python")) 

print(text2.find("my")) #aranan kelimenin indexini döndürür 
print(text2.find("pyton")) #yoksa -1 döndürür




