import psycopg2

# Establish a connection to the database
conn = psycopg2.connect(
    dbname="Assignment3",
    user="postgres",
    password="student",
    host="localhost",
    port="5432"  # default PostgreSQL port
)

# Create a cursor object
cur = conn.cursor()

# Function that creates the table
def createTable():
    create_table_command = """
    CREATE TABLE students (
        student_id SERIAL PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        enrollment_date DATE
    );
    """
    cur.execute(create_table_command)
    conn.commit()

# Function that inserts the data
def insertData():
    insert_data_command = """
    INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
    ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
    """
    cur.execute(insert_data_command)
    conn.commit()

# Function that retrieves and displays all records from the students table
def getAllStudents():
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    for student in students:
        print(student)

# Function that inserts a new student record into the students table
def addStudent(first_name, last_name, email, enrollment_date):
    insert_query = """
    INSERT INTO students (first_name, last_name, email, enrollment_date) 
    VALUES (%s, %s, %s, %s)
    """
    cur.execute(insert_query, (first_name, last_name, email, enrollment_date))
    conn.commit()

# Function that updates the email address with a specified student_id
def updateStudentEmail(student_id, new_email):
    update_query = """
    UPDATE students 
    SET email = %s
    WHERE student_id = %s
    """
    cur.execute(update_query, (new_email, student_id))
    conn.commit()

# Function that deletes the record of the student with the specified student_id
def deleteStudent(student_id):
    delete_query = """
    DELETE FROM students 
    WHERE student_id = %s
    """
    cur.execute(delete_query, (student_id,))
    conn.commit()

while True:
    choice = input("Main Menu: \n1. Create table\n2. Insert data into table\n3. Get all students\n4. Add student\n5. Update student email\n6. Delete student\n0. Exit\n")
    if choice == "1":
        createTable()
    elif choice == "2":
        insertData()
    elif choice == "3":
        getAllStudents()
    elif choice == "4":
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        enrollment_date = input("Enter enrollment date (yyyy-mm-dd): ")
        addStudent(first_name, last_name, email, enrollment_date)
    elif choice == "5":
        student_id = input("Enter student ID: ")
        new_email = input("Enter new email: ")
        updateStudentEmail(student_id, new_email)
    elif choice == "6":
        student_id = input("Enter student ID: ")
        deleteStudent(student_id)
    elif choice == "0":
        cur.close()
        conn.close()
        break


