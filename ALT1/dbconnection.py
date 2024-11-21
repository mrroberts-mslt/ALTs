import mysql.connector

db = mysql.connector.connect(
    host="213.165.241.247",
    user="lccs_huw2",
    password="XXXXXX",
    database="lccs_huw"
)


cursor = db.cursor()

cursor.execute("SHOW DATABASES")

for i in cursor:
  print(i)
