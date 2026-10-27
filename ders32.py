#BeautifulSoup 
my_html_doc="""
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python | Berke Akgöz </title>
</head>
<body>
    <h1>Python Eğitimi </h1>
    <div id="first id">
        <h2>Html Sayfası</h2>
        <ul>
            <li>1</li>
            <li>2</li>
            <li>3</li>
            <li>4</li>
            <li>5</li>
        </ul>

    </div>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. At culpa, cum hic veniam eligendi vel,
         explicabo accusantium molestiae aliquid dignissimos nemo natus corporis quo unde eum earum consequatur voluptates quaerat.
    </p>
     <div class="mylinks">
        <h2>Css Sayfası</h2>
        <a href="http://example.com">Link1</a>
        <a href="http://example.com">link2</a>
        <a href="http://example.com">link3</a>
     </div>
</body>
</html>
"""
from bs4 import BeautifulSoup

soup=BeautifulSoup(my_html_doc,'html.parser')

result=soup.prettify() #tüm html dökümanını aldık 
print(result)

print(soup.title) #htmldeki title aldık
print(soup.title.string) #titlenın içindeki stringi getirir
print("----------------------")
print(soup.head) #head istersek body istersek body kod blogunu getirir 
print(soup.h2.string) #birden fazla aynı etiket varsa ilkini getirir 
print("----------------------")
print(soup.find_all("h2")) #birden fazla varsa ve hepsini görmek istersek find_all() metodunu kullanmalıyız 
print(soup.find_all("h2")[1])#eğer ikinciyi istiyorsak dizi mantığı 1 0dır 2. ise 1dir bu şekilde ulaşırız
print("----------------------")
result=soup.find_all("div") #tüm divleri liste olarak döndürür

for item in result:
    print(item)

print("----------------------")

result=soup.find_all("div")[0].ul #ilk divimin içindeki ul getirir
print(result)

print("----------------------")

result=soup.find_all("div")[0].ul.find_all("li") #ilk divimin içindeki ullerin içindeki li getir
print(result)

for item in result:  #ilk divimin içindeki ullerin içindeki lilerin stringleri yazdırır
    print(item.string) 

print("---------------------")

result=soup.div.findChildren() #birinci divin cocuklarını getir(Hiyerarşı mantığı)
print(result)

print("---------------------")

#result=soup.div.next_sibling() #Sıradaki kardeşini getir diyor yani öbür div 

#print(result)
print("---------------------")


