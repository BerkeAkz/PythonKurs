import mysql.connector


class MySQLDatabase:
    def __init__(self,database):
        self.__host="localhost"
        self.__user="root"
        self.__password=""
        self.__database=database
        self.__connection=None
        self.__cursor=None
        

    def connection(self):
        self.__connection=mysql.connector.connect(
            host= self.__host,
            user=self.__user,
            password=self.__password
            ,database=self.__database
            )
        if self.__connection.is_connected():
            self.__cursor=self.__connection.cursor()
            print("Başarılı")
        else:
            print("Başarısız")


    def create_db(self,db_name):
        sql=f"CREATE DATABASE IF NOT EXISTS {db_name}"
        self.__cursor.execute(sql)
        print(f"{db_name} Veri Tabanı Başarıyla Oluşturuldu")

    def add_user(self,user_name,user_age):
        sql="INSERT INTO customers(customer_name,customer_age) values(%s,%s)"
        values=(user_name,user_age)
        self.__cursor.execute(sql,values)
        self.__connection.commit() #verinin eklenmesini sağlar
        print(f"{user_name} Eklendi")
        print(f"Last ID:{self.__cursor.lastrowid}")



    def create_table(self,db_name,tablo_name,Colums):
        self.__cursor.execute(f"USE {db_name}") #bu db kullan
        sql=f"CREATE TABLE IF NOT EXISTS {tablo_name}({Colums})"
        self.__cursor.execute(sql)
        print(f"{tablo_name} Veri Tabanına Tablo Başarıyla Oluşturuldu")
        





    def disconnect(self):
        if self.__cursor:
            self.__cursor.close()
        if self.__connection:
            self.__connection.close()
