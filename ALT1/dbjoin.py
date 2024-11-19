import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

#the \ allow you to split up the sql query to make it more readable

sql = "SELECT \
  patients.fName AS pfname, \
  doctors.docFirstName AS docfname \
  FROM patients \
  INNER JOIN doctors ON patients.doctor_id = doctors.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)