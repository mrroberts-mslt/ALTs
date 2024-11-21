import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

cursor = db.cursor()

sql = "UPDATE patients SET lname = %s WHERE lname = %s"
val = ("McCarthy", "McLennon")

cursor.execute(sql, val)

db.commit()

print(cursor.rowcount, "record(s) affected")
