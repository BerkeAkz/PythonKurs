#Bir Apıden json Verileri çekmek 
import requests

my_url='https://jsonplaceholder.typicode.com/todos'

result=requests.get(my_url)

result=result.json() #json metoduyla json verilerini dönüştürdü


#print(result) tüm listeyi getirir

print(result[0]["id"])
print(result[0]["title"]) 

print("-----------")

for item in result:
    print(f"{item["id"]}--{item["title"]}")


#uygulama
excharge_currency=input("Enter excharge currency:")
foreign_excharge_received=input("enter excharge received:")
amount=int(input("How Many money Do You Want to Excharge:"))

my_url=f'https://v6.exchargerate-api.com/v6/***/latest/{excharge_currency}'

result=requests.get(my_url)

result=result.json()

new_amount=amount*result["conversion_rates"][foreign_excharge_received]

print(f"{amount}{excharge_currency}={new_amount:..2f}{foreign_excharge_received}")

