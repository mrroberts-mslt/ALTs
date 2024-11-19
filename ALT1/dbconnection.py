import mysql.connector

db = mysql.connector.connect(
    host="213.165.241.247",
    user="lccs_huw2",
    password="XXXXXX",
    database="lccs_huw"
)


mycursor = db.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
