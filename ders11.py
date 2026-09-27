#döngüler
#while

i=1
while (i<=7): #koşul doğru oldukça içeri girer
    print(i)
    i+=1

print("----------------------------------------------------")
j=1
while(j<=7):
    print(j)
    if j==5:
            break
    j+=1


# continue beni görünce es geç ama başa dön benden sonrakileri es geç
#break beni görünce dur ve döngüden çık
print("----------------------------------------------------")
print("----------------------------------------------------")
print("----------------------------------------------------")
numaralar=[70,49,67,10,39]

i=0

while (len(numaralar)>i):
     print(numaralar[i])
     i+=1
print("----------------------------------------------------")
print("----------------------------------------------------")
print("----------------------------------------------------")

i=70

while (i>=0):
     print(i)
     i-=5

print("----------------------------------------------------")
print("----------------------------------------------------")
print("----------------------------------------------------")

 #For Döngüsü

meyveler=["elma","armut","erik","çilek","portakal","mandalina","şeftali"]

for x in meyveler:
     if (x=="erik"):
       continue
     print(x)
else :
     print("bitti")

print("----------------------------------------------------")
print("----------------------------------------------------")
print("----------------------------------------------------")  

sayi=int(input("Bir Sayı Gir:"))

for x in range(sayi):
     if(x%2==0):
          continue
     print(x)

     



