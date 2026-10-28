
from db_class import MySQLDatabase

db=MySQLDatabase("python")

db.connection() #bağlantıyı yaptı
#db.create_db("python")
#db.create_table("testdb","people","user_id INT AUTO_INCREMENT PRIMARY KEY,user_name VARCHAR(100), user_lastname VARCHAR(100),user_age INT")

db.add_user("Berke",21)

db.disconnect() #bağlantıyı kapat
