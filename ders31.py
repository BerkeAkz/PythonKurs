#Request modulu get post put delete 
import requests
my_url="https://jsonplaceholder.typicode.com/posts"

payload={
    "userId":7,
    "id":68
}
result=requests.get(my_url,params=payload)#belli bir bilgiyi isstersek bunu 2. parametreyle ulaşabiliriz

print("URl:",result.url)
print("Status Code:",result.status_code)
print("Json:",result.json())

print("-------------------------")
#post

my_url="https://jsonplaceholder.typicode.com/posts"

data={
    "date":"2026-01"
}
result=requests.post(my_url,json=data)

print("URl:",result.url)
print("Status Code:",result.status_code)
print("Json:",result.json())


print("-------------------------")
#post

my_url="https://jsonplaceholder.typicode.com/posts/1"

data={
    "title":"Updated Title",
    "body":"This is updated content",
    "userId":1
}
result=requests.put(my_url,json=data)

print("URl:",result.url)
print("Status Code:",result.status_code)
print("Json:",result.json())

print("-------------------------")
#patch

my_url="https://jsonplaceholder.typicode.com/posts/1"

data={
    "title":"Updated Title"
    
}
result=requests.patch(my_url,json=data)

print("URl:",result.url)
print("Status Code:",result.status_code)
print("Json:",result.json())

print("-------------------------")
#delete

my_url="https://jsonplaceholder.typicode.com/posts/1"

result=requests.delete(my_url)


print("Status Code:",result.status_code)
