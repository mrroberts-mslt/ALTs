import mysql.connector

db = mysql.connector.connect(
    host="213.165.241.247",
    user="lccs_huw2",
    password="YNbW8iHH8MKH",
    database="lccs_huw"
)


mycursor = db.cursor()

mycursor.execute("SELECT * FROM patients")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

idChange = int(input("Enter the patient id to change: "))
newLname = input("Enter a new last name: ")

sql = "UPDATE patients SET lName = %s WHERE patient_id = %s"
val = (newLname, idChange)

mycursor.execute(sql, val)

db.commit()

print(mycursor.rowcount, "record(s) affected")
