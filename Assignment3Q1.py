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

# Function that updates the email address with a specified student_id
def updateStudentEmail(student_id, new_email):
    update_query = """
    UPDATE students 
    SET email = %s
    WHERE student_id = %s
    """
    cur.execute(update_query, (new_email, student_id))

# Function that deletes the record of the student with the specified student_id
def deleteStudent(student_id):
    delete_query = """
    DELETE FROM students 
    WHERE student_id = %s
    """
    cur.execute(delete_query, (student_id,))

# Call the functions
# getAllStudents()
# addStudent('Kina', 'Zhan', 'kina.zhan@cmail.carleton.ca', '2024-03-12')
# print("UPDATED STUDENTS:")
# getAllStudents()

# getAllStudents()
# updateStudentEmail(1, 'new.email@example.com')
# print("UPDATED STUDENTS:")
# getAllStudents()

# getAllStudents()
# deleteStudent(2)
# print("UPDATED STUDENTS:")
# getAllStudents()
    
# Closes the cursor and connections
conn.commit()
cur.close()
conn.close()

