import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

cursor = db.cursor()

cursor.execute("SELECT * FROM doctors")

myresult = cursor.fetchall()

for x in myresult:
  print(x)
