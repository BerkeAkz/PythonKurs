#Dosya İşlemleri
import os
print(os.stat("files/demo.txt").st_size)
#f=open(filename,mod,buffering,encoding,errors,newline,closefd,opener)
f=open("PythonKurs/demo.txt","r+",encoding="utf-8")
print(f.read(10)) #ilk on indisli geri döndürür parametre yoksa hepsini okur
#f.seek() #imleci kontrol etmek için

f.close() #dosyayı kapatmak için

print(f.close()) # dosya kapalı mı doğruysa 1 yanlıssa 0 döner

with open("files/demo.txt",encoding="utf-8") as f: #kullanışlı dosyayı kapatmaya close metoduna gerek yok
  print(f.read())

print(f.tell()) #tell imlecin nerede olduğunu söyler 

print(f.readable()) #okuma modunda mı açılmış 1 evet 0 hayır

#trancute w a r+ w+ modlarında çalışır
with open("files/demo.txt","r+",encoding="utf-8") as f: 
  f.truncate(10)
  print(f.read(),end="") #imlecin olduğu yerden sonrasını siler