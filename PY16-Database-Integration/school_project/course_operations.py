from db_config import get_connection

def create_courses_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            course_name VARCHAR(100) NOT NULL,
            credits INT,
            instructor VARCHAR(100)
        )
    """)

    connection.commit()
    cursor.close()
    connection.close()


def add_course(course_name, credits, instructor):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO courses (course_name, credits, instructor) VALUES (%s, %s, %s)",
        (course_name, credits, instructor)
    )

    connection.commit()
    cursor.close()
    connection.close()


def get_all_courses():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()

    for course in courses:
        print(course)

    cursor.close()
    connection.close()


def update_course_instructor(course_id, new_instructor):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE courses SET instructor = %s WHERE id = %s",
        (new_instructor, course_id)
    )

    connection.commit()
    cursor.close()
    connection.close()


def delete_course(course_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM courses WHERE id = %s",
        (course_id,)
    )
    # Comma is required because it is a tuple with one value. 

    connection.commit()
    cursor.close()
    connection.close()