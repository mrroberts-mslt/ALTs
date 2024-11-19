import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = db.cursor()
sql = "INSERT INTO doctors (docFirstName, docLastName) VALUES (%s, %s)"
val = ("Emily", "Clark")

mycursor.execute(sql, val)

db.commit()

print(mycursor.rowcount, "record inserted.")

