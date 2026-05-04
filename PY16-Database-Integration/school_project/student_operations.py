from db_config import get_connection

def create_students_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            student_name VARCHAR(100) NOT NULL,
            email VARCHAR(100),
            course_id INT,
            FOREIGN KEY (course_id) REFERENCES courses(id)
        )
    """)

    connection.commit()
    cursor.close()
    connection.close()


def add_student(student_name, email, course_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO students (student_name, email, course_id) VALUES (%s, %s, %s)",
        (student_name, email, course_id)
    )

    connection.commit()
    cursor.close()
    connection.close()


def get_all_students():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT 
            students.id,
            students.student_name,
            students.email,
            courses.course_name,
            courses.instructor
        FROM students
        INNER JOIN courses
        ON students.course_id = courses.id
    """)

    students = cursor.fetchall()

    for student in students:
        print(student)

    cursor.close()
    connection.close()


def update_student_email(student_id, new_email):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE students SET email = %s WHERE id = %s",
        (new_email, student_id)
    )

    connection.commit()
    cursor.close()
    connection.close()


def delete_student(student_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = %s",
        (student_id,)
    )

    connection.commit()
    cursor.close()
    connection.close()