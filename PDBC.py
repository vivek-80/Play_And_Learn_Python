# A database is an organised collection of data. it can be accessed and manage by the user very
# easily.It allow us to organize data into tables with row and column. Databases avaiable
# including mysql,postgresql,sql server,oracle etc.

# mysql is a relational database management system (RDBMS) based on the sql queries. It is
# one of the most popular language for accessing and managing the data in schemas.

# Firstly, We have to install mysql-connector, which is nothing but a package.

import mysql.connector

# esatablish connection in b/w python and mysql.

mydb= mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Perl123@"
)
mycursor = mydb.cursor()

# use client_db:
mycursor.execute('use client_db')


# Create table Client:
# mycursor.execute('create table client(id int not null,name varchar(25),age int)')

# insert data into client table:
# mycursor.execute("insert into client(id,name,age) values(101,'shiva',21)")

# Create table consumer:
# sql='create table consumer(id int not null unique,name varchar(45),Product_name varchar(55))'

# Insert data into table:
# sql_insert='insert into consumer(id,name,Product_name) values(%s,%s,%s)'
# val=[(55,'shubham','realme'),(85,'ravi','samsung'),]

# Take Executemany Method:
# mycursor.executemany(sql_insert,val)

# Alter table means modification:
# sql_alter='alter table consumer add occupation varchar(45)'

# mycursor.executescript('create table consumer(id int not null unique,name varchar(45),Product_name varchar(55))';'alter table consumer add occupation varchar(45)')

# Select Command with where:
# mycursor.execute('select * from consumer where id=85 and name="ravi"')

# Select command only:
# mycursor.execute('select * from consumer')

# Fetch Commmands:
# data=mycursor.fetchone()
# print(data)
# data=mycursor.fetchall()
# for detail in data:
    # print(detail)

# Delete Command:
# mycursor.execute('DELETE FROM consumer WHERE id=45')

# select command with id,name:
# mycursor.execute('select id,name from consumer')

# select all columns:
# mycursor.execute('select * from consumer')
# data=mycursor.fetchone()
# for row in data:
#     print(row)

# Alter table to add primary key:
# mycursor.execute('alter table consumer add PRIMARY KEY (ID)')

# mycursor.execute('SELECT client.age, Consumer.name, consumer.Product_name FROM client INNER JOIN consumer ON client.age=consumer.name')
# data=mycursor.fetchone()
# print(data)

# To save any modification:
# mydb.commit()

# To Close connection with mysql:
# mydb.close()

# To undo the task:
# mydb.Rollback()
