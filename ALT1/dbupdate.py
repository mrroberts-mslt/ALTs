import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = db.cursor()

sql = "UPDATE patients SET lname = %s WHERE lname = %s"
val = ("McCarthy", "McLennon")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
