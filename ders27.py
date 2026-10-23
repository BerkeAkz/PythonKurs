#Json

#uygulamalar arası veri transferi için 
#APIden yani veri servisinden veri bu formatta alınır
#veri tabanına alternatif için küçük projelerde kullanılır 


#python bu dictionary veri türüdür
#person={"name":"Berke", "age":"21","city":"Zonguldak","hobbies":["Kodlama","Spor","futbol"]} bu haliyle dict. json değil

import json
#json verisini dict cevirme

person='{"name":"Berke", "age":"21","city":"Zonguldak","hobbies":["Kodlama","Spor","futbol"]}' #bu hali ile json formatında

result=json.loads(person) #json.loads() metoduyla bunu bir dict veri türüne dönüştürüyoruz


print(f"Name:{result["name"]}")
print(f"Age:{result["age"]}")
print(f"City:{result["city"]}")

print(f"hobbies:",end="")

for item in result ["hobbies"]:
    print(item,end=" ")

print("-------------------------")
print("-------------------------")
print("-------------------------")
print("-------------------------")


# Bir dosyadan json Formatından Veri çekme 

person={"name":"Berke", "age":"21","city":"Zonguldak","hobbies":["Kodlama","Spor","futbol"]}


with open("files/data.json","r",encoding="utf-8") as f:
    result=json.load(f) #dosyada load() kullanırız jsondan bunu dict ceviririz 

    print(f"Name:{result["name"]}")
    print(f"Age:{result["age"]}")
    print(f"City:{result["city"]}")
     
    print(f"hobbies:",end="")
     
    for item in result ["hobbies"]:
       print(item,end=" ")




print("-------------------------")
print("-------------------------")
print("-------------------------")
print("-------------------------")

#dictionary veri türünden json formatına çevirme işlemi

person={"name":"Berke", "age":"21","city":"Zonguldak","hobbies":["Kodlama","Spor","futbol"]}

result=json.dumps(person,ensure_ascii=False) #dumps dict den jsona çevir 2. parametresi ascii kapatır türkçe ifadeler kullanılır  
print(type(result)) #json bir stringdir ve string yazacak
print(result)


print("-------------------------")
print("-------------------------")
print("-------------------------")
print("-------------------------")


with open("files/people.json","w",encoding="utf-8") as f:
    jsonresult=json.dump(person,f,ensure_ascii=False,indent=4)


