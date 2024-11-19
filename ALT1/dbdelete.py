import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = db.cursor()

sql = "DELETE FROM patients WHERE patient_id = 1"

mycursor.execute(sql)

db.commit()

print(mycursor.rowcount, "record(s) deleted")
