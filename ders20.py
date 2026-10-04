#Nesneye Yönelik Programlama

class myClass:
    x=7 #property


obj=myClass()
print(obj.x)


class arac:
    marka="Hyundai"
    model="i20"
    color="Gri"
    def __init__(self): #constructor
        print("Bu Bir Constructordır")

arabaObjesi=arac()
print("Marka:",arabaObjesi.marka)
print("Model:",arabaObjesi.model)
print("Renk",arabaObjesi.color)

print("--------------------------------")

class arac2:
        def __init__(self,marka,model,renk): #constructor
          self.marka=marka
          self.model=model
          self.renk=renk 

arabaobjesi2=arac2("hyundai","i20","Gri")
arabaobjesi3=arac2("Citroen","C","Beyaz")

print(arabaobjesi2.marka)
print(arabaobjesi3.marka)

print("--------------------------------")
print("--------------------------------")
print("--------------------------------")


class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a

    def __str__(self):
        return f"Name:{self.name}\n Age:{self.age}"


p1=Person("Fehmi Uyar",21)

print(p1)

print("--------------------------------")

class insan:
     def __init__(self,n,a):
            self.name=n
            self.age=a

     def myinfo(self):
          print(f"Hello my name is {self.name}")
          print(f"i am {self.age} years old")


p4=insan("Berke Akgöz",21)
print(p4)
print("-------")
p4.myinfo()
p4.age=34
p4.myinfo()

del p4 #nesneyi siler
print("---------------------------------------")
print("---------------------------------------")
print("---------------------------------------")
#kalıtım inheritance
  
class Person: #parent class yada base class
     def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

     def myprint(self):
      print(self.firstname,self.lastname)
class idari(Person):
    pass
class akademikp(Person):
    pass
class Student(Person): #miras almak istediğimiz sınıfı parantez içine yazdık
    def __init__(self,fname,lname,gra):
        super().__init__(fname,lname)
        self.gra=gra

    def welcome(self):
        print(f"Welcome {self.firstname} {self.lastname}")

p1=Student("Berke","Akgöz",2028)
p1.myprint()
p1.welcome()

print("---------------------------------------")
print("---------------------------------------")
print("---------------------------------------")

class Animal:  #parend class
    def speak(self):
        return "sound"

class Dog(Animal): #child class
        def speak(self): #method overriding metot ezme 
         return "Bark"

class Cat(Animal): #child class
        def speak(self): #method overriding metot ezme
         return "Meow"

dog=Dog()
cat=Cat()

print(dog.speak())
print(cat.speak()) 

#multiple inheritance çoklu kalıtım

class a:
    def aa(self):
        return "A Classı"

class b:
    def bb(self):
        return "B Classı"

class c(a,b):
    def cc(self):
        return "C Classı"

print("---------------------------------------")
print("---------------------------------------")
print("---------------------------------------")



