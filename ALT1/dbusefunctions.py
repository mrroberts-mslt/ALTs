import mysql.connector

def updatePatientLname(cursor, db, old_lname, new_lname):
    sql = "UPDATE patients SET lname = %s WHERE lname = %s"
    val = (new_lname, old_lname)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "record(s) affected")

def insertDoctor(cursor, db, first_name, last_name):
    sql = "INSERT INTO doctors (docFirstName, docLastName) VALUES (%s, %s)"
    val = (first_name, last_name)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "record inserted.")

def main():
    # Establish database connection
    db = mysql.connector.connect(
    host="213.165.241.247",
    user="lccs_huw2",
    password="YNbW8iHH8MKH",
    database="lccs_huw")
    cursor = db.cursor()

    # User selects operation
    print("Select operation:")
    print("1: Insert doctor")
    print("2: Update patient last name")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        first_name = input("Enter doctor's first name: ")
        last_name = input("Enter doctor's last name: ")
        insertDoctor(cursor, db, first_name, last_name)
    elif choice == "2":
        old_lname = input("Enter patient's old last name: ")
        new_lname = input("Enter patient's new last name: ")
        updatePatientLname(cursor, db, old_lname, new_lname)
    else:
        print("Invalid choice!")

    # Close the database connection
    cursor.close()
    db.close()

# Directly call the main function
main()

