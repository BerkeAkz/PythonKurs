import os 

class PhoneBook:
    FİLE_NAME="files/phonebook.txt"
    def __init__(self):
       if not os.path.exists(self.FİLE_NAME):
           with open(self.FİLE_NAME,"w",encoding="utf-8") as f:
            pass

    def add_contact(self,firstname,lastname,phone):
        with open(self.FİLE_NAME,"a",encoding="utf-8") as f:
          f.write(f"{firstname},{lastname},{phone}\n")
          print(f"{firstname} {lastname} has been added to the Phone Book")

    def list_contact(self,):
       with open(self.FİLE_NAME,"r",encoding="utf-8") as f:
          lines=f.readlines()
          if not lines:
             print("The phone book is empty")
          else:
             print("\nPhone Book:")
             for line in lines:
                firstname,lastname,phone=line.strip().split(",")
                print(f"{firstname} {lastname} - {phone}")

    def delete_contact(self,name):
        with open(self.FİLE_NAME,"r",encoding="utf-8") as f:
                 lines=f.readlines()
                 contact_found=False
        with open(self.FİLE_NAME,"w",encoding="utf-8") as f:
           for line in lines:
                firstname,lastname,phone=line.strip().split(",")
                if(firstname!=name):
                    f.write(line)
                else:
                    contact_found=True

        if(contact_found):
            print(f"Contact named {name} has been deleted from the phone book")
        else:
            print(f"No contact named {name} was found")        
                  