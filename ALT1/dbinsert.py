import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

cursor = db.cursor()
sql = "INSERT INTO doctors (docFirstName, docLastName) VALUES (%s, %s)"
val = ("Emily", "Clark")

cursor.execute(sql, val)

db.commit()

print(cursor.rowcount, "record inserted.")

