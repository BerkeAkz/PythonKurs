#Python ile Veri Tabanı
import mysql.connector
                                  # Eğer sunucu kiralarsak buraya local host yazmamalıyız 24.45.123 gibi 
connection=mysql.connector.connect(host="localhost",user="root",password="")

if(connection.is_connected()): #bağlantı kuruldu mu 
    print("Bağlantı Kuruldu")
else:
    print("Bağlantı Kurulmadı")

connection.close() #Bağlantıyı kapatır 

print("-------------------------------------")
print("-------------------------------------")
print("-------------------------------------")
print("-------------------------------------")

import mysql.connector

connection=mysql.connector.connect(host="localhost",user="root",password="",database="newdb")

mycursor=connection.cursor() #sql komutlarını çalıştırması için bir nesne kuruyor 

#mycursor.execute("CREATE DATABASE IF NOT EXISTS newdb")

#mycursor.execute("SHOW DATABASES")

#for item in mycursor:
    #print(item)

#tablo oluşturma 

#mycursor.execute("CREATE TABLE users(user_id INT AUTO_INCREMENT PRIMARY KEY,user_name VARCHAR(100), user_lastname VARCHAR(100),user_age INT)")
#mycursor.execute("SHOW TABLES")
#for item in mycursor:
    #print(item)

#mycursor.execute("ALTER TABLE users ADD COLUMN user_email VARCHAR(120)")

mycursor.close()
connection.close()