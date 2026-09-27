
sayi=int(input("Faktöriyeli almak istediğin sayısı yaz:"))
sonuc=1
if (sayi==1):
    print(1)

while(1<=sayi):
    sonuc=sonuc*sayi

    sayi-=1

print(sonuc)