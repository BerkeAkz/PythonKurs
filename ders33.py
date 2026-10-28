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
    <div id="first_id">
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

print(soup.title.parent.name) #titlenin ebeveyni

print(soup.div["id"])

print(soup.find_all("div")[0].attrs) #ilk divimin attrslerini ver 

print(soup.find("a"))#istediğimiz etiketin ilkini döndürür

print("----------------------")
print(soup.head.contents)#head içindeki cocukları getir list şeklinde döndür
#\n bunlarıda dahil eder o yüzden birinci cocuk 1. indistedir

print(soup.head.contents[5].contents) #head içindeki 5. indisdeki cocuğa ulaş onunda çocuklarını getir

print("----------------------")

for child in soup.head.descendants: #torunlarıda cocuklarıda dahil eder
    print(child)

print(soup.title.parent) #titlenin paranti headtir
print(soup.title.parent.parent) #onunda parenti htmldir
print("---------------------")
print(soup.h1.next_sibling.next_sibling) #arada\n var onlara dikkat ileri kardeşler arası dolaşma 

print(soup.a.previous_sibling.previous_sibling) #geriye doğru kardeşine gider h2dir 

print("---------------------------------")
print("---------------------------------")
print("---------------------------------")
print(soup.find_all(["a","p"])) #hem paragrafı hemde linki getirir
print("---------------------------------")
print("---------------------------------")
print(soup.css.select("#first_id")) #idsi first_id olanı getir
print("---------------------------------")
print(soup.css.select("body a")) #body içerindeki linkleri getir