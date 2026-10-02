#istatistik Modülü

import statistics

data=[10,20,30]

print(statistics.harmonic_mean(data))

data1=[1,3,5,7,9,11,13]
print(statistics.mean(data1)) 

print(statistics.median(data1)) 
data1=[1,3,5,7,9,11]
print(statistics.median(data1))


data2=[10,12,23,23,16,23,21,16]

print(statistics.pstdev(data2)) #standart sapma
print(statistics.variance(data2)) #varyans


print("--------------------------------")
print("--------------------------------")
print("--------------------------------")
print("--------------------------------")

#datetime Modülü

import datetime

result=dir(datetime) #sınıfın içinde neler var onu gösterdi
print(result)

result=datetime.datetime.now() #şuanın tarihini aldı
print(result) 

from datetime import datetime ,timedelta # datetime sınıfından her şeyi istemeyebiliriz gerekenei alırız
result=datetime.now()
print(result)

result=datetime(2005,8,30,2,30) # istediğimiz tarihi böyle yazdırabiliriz
print(result)

import locale
result=datetime.today() 
result=datetime.now()
 
print(result.day) #sadece günü aldık
print(result.month) 
print(result.year) 
print(result.hour)
print(result.second)  

print(datetime.weekday(result)) #haftanın hangi günü pazartesi 0 indeksinden başlar 
locale.setlocale(locale.LC_TIME,"tr-TR.UTF-8") #Türkçe ayarı

print(result.strftime("%a %A %w %d %b %Y ")) 

date1=datetime(2026,9,2)
date2=datetime(2005,8,30)

fark=date1-date2

print(fark.days)


today=datetime.now()

gelecek=today+timedelta(days=5) # 5 gün ileri alabilme
gecmis=today-timedelta(days=7) 

print(today)
print(gelecek)
print(gecmis)

