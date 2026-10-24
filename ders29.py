import requests
my_url='https://w3schools.com/python/demopage.js' 
result=requests.get(my_url,) 


print(result.text) #html kodlarını getirir 

print(result.status_code) #durum kodunu döndürür 

#1xx 100,101 istek alındı işleniyor
#2xx 200,201,204 istek başarıyla alındı ve kabul edildi 
#3xx 301,302,304 tamamlanması için ek işlem gerekiyor 
#4xx istek hatalı veya erişilemiyor 
#5xx  sunucu hatası 

print(result.cookies)
print(result.elapsed) #sunucuya istekte bulunduk gidişinden dönüşüne kadar geçen süreyi getirir
print(result.headers)

print(result.ok)
print(result.reason) #durum komuduna  karşılık gelen metin değerini döndürür
print(result.url)

#print(result.json())#json verilerini çeker



result.close() #sunucuyla bağlantıyı kapatmak istersek bunun yazmalıyız 
print("----------------------------------------------------")
#uygulama 

try:
    my_url='https://w3schools.com/python/demopage.js' 
    result=requests.get(my_url,) 
    result.raise_for_status()
    print(result.status_code)
except requests.exceptions.HTTPError as e:
    print("Https Hatası:",e)
except Exception as err:
    print("Başka Bir Hata Oluştu:",err)
else:
    print("İstek Başarılı")

result.close()
