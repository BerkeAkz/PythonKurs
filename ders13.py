meyveler=["elma","armut","erik","çilek","portakal","mandalina","şeftali"]
"""
for item in meyveler:
    print(item , end="-")


for item in range(len(meyveler)): #0dan 8. indekse kadar 
    print(meyveler[item])

print("-----------------------------------------")
i=0

while (i<len(meyveler)):
    print(meyveler[i])
    i+=1 """

#List Comprehension liste kavrama
print("-----------------------------------------")
print("-----------------------------------------")
[print(item) for item in meyveler]
print("-----------------------------------------")
print("-----------------------------------------")
yeniliste=[item for item in meyveler if("e" in item)]

[print(item) for item in yeniliste]

yeniliste2=[item.upper() for item in meyveler]
print(yeniliste2)