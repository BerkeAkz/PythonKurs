text="the price is only {price:.2f} turkish lira!"

print(text.format(price=70)) 

text2=" Benim adım {isim} {yas} yaşındayım.".format(isim="berke",yas=21)
print(text2)

text3=" Benim adım {0} {1} yaşındayım.".format("berke",21)
print(text3)

text4="we do not have {:<10} children" # sola hızalama 
print(text4.format(7))

text4="we do not have {:>10} children" # sağa hızalama 
print(text4.format(7))

text4="we do not have {:^10} children" # ortaya hızalama 
print(text4.format(7))

