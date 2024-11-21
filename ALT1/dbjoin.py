import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

cursor = db.cursor()

#the \ allow you to split up the sql query to make it more readable

sql = "SELECT \
  patients.fName AS pfname, \
  doctors.docFirstName AS docfname \
  FROM patients \
  INNER JOIN doctors ON patients.doctor_id = doctors.id"

cursor.execute(sql)

myresult = cursor.fetchall()

for x in myresult:
  print(x)
