import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = db.cursor()

mycursor.execute("SELECT * FROM doctors")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
