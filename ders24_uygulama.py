from Phone_class import PhoneBook

pb=PhoneBook()

while True:
  print("\nPhone Book")
  print("1-Add Contact")
  print("2-list Contact")
  print("3-Delete Contact")
  print("4-Exit")

  choice=int(input("Make Your Choice:"))

  if(choice==1):
     firstname=(input("First Name:"))
     Lastname=(input("Last Name:"))
     phone=(input("Phone:"))
     pb.add_contact(firstname,Lastname,phone)

  elif(choice==2):
     pb.list_contact()
     
  elif(choice==3):
       pass
  elif(choice==4):
     print("Exiting....")
     break
  else:
     print("Invalid choice , please try again")