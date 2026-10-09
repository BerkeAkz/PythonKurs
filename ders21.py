#Erişim Belirleme (encapsulation-kapsülleme)
#Public protected private

#public te bişi kullanmıyor 
#proected _
#private ___


#public
class Car:
    def __init__(self,b,m):
       self.marka=b
       self.model=m
    def display_info(self):
        return f"Car:{self.marka} {self.model}" 

c1=Car("Hyundai","i20")

print(c1.marka)
print(c1.model)
print(c1.display_info())

#protected
class Animal:
    def __init__(self,n,s):
        self.name=n  #public
        self._species=s #protected

    def _makeSound(self):  #protected method
        return "Animal sound"


class Dog(Animal):
    def __init__(self, n, b):
        super().__init__(n, "dog")
        self.breed=b

    def display_info(self): #public m
        return f"{self.name},{self.breed},{self._species} " #_speciesi kullanabildi
    def makeSound(self): #protected m
        return self._makeSound()

dog=Dog("Kurt","Golden")
print(dog.display_info())
#print(dog._makeSound())  buna ulaşamaz 


#private
class bankhesabı:
    def __init__(self,n,b):
        self.hesapno=n  #publiic
        self.__balance=b #private

    def deposit(self,amount):  #public
        if(amount>0):
            self.__balance+=amount
            return f"deposited:{amount} new balance:{self.__balance}"
        return "ınvalid deposit amount"

    def __display_balance(self):  #private
        return f"Balance:${self.__balance}"

    def get_balance(self): #public
        return self.__display_balance()


account=bankhesabı("12345678",2000)
#print(account.__balance) buna erişemez
print(account.get_balance())


print("-------------------------------")
print("-------------------------------")
print("-------------------------------")

#polimorfizim (çok biçimlilik)

