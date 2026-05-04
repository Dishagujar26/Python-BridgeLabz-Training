# install the required package - pip install mysql-connector-python

import mysql.connector # connect Python to MySQL
from mysql.connector import Error # catches database errors

# Configuration
config = {
    'host': 'localhost',
    'database': 'schooldb',
    'user': 'root',
    'password': 'admindisha26'
}

try:
    # Connect to MySQL
    connection = mysql.connector.connect(**config)
    '''
    cursor is an object that is used to execute SQL queries. 
    notmal cursor return tuples - probelm is that we have to access the data using indexes 
        [
            (1, 'Python Programming', 3, 'Dr. Smith'),
            (2, 'Java', 4, 'John')
        ] access like - row[1] or row[2] have to remember the index 

    when we are doing dictionary = true we are telling the cursor to return the data as a dictionary 
    where the column names are the keys and the column values are the values 
            [
               {
                    "id": 1,
                    "course_name": "Python Programming",
                    "credits": 3,
                    "instructor": "Dr. Smith"
                }
            ] access like - row['course_name'] or row['instructor']

    '''
    cursor = connection.cursor(dictionary=True)  
    
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            course_name VARCHAR(100) NOT NULL,
            credits INT,
            instructor VARCHAR(100)
        )
    ''')
    
    # Insert with auto-commit
    connection.autocommit = False  # Manual commit for transaction control
    cursor.execute(
        "INSERT INTO courses (course_name, credits, instructor) VALUES (%s, %s, %s)", # python mysql uses %s for placeholder
        ("Python Programming", 3, "Dr. Smith")
    )
    connection.commit()  # Explicit commit


    '''
            
        # METHOD 2: Insert multiple records at once (much faster for many records)
        # This is called "batch insert"
        students_list = [
            ("Bob Smith", 22, 'B', '2024-01-20', 3.2),
            ("Charlie Brown", 19, 'C', '2024-02-01', 2.8),
            ("Diana Prince", 21, 'A', '2024-01-10', 3.9),
            ("Ethan Hunt", 25, 'B', '2024-01-25', 3.5),
            ("Fiona Apple", 20, 'A', '2024-02-05', 3.7)
        ]

        # executemany() is for inserting multiple rows at once
        cursor.executemany(insert_query, students_list)
    
    '''
    
    # Query with dictionary cursor (easier to access by column name)
    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()
    for course in courses:
        print(f"Course: {course['course_name']}, Instructor: {course['instructor']}")
        
except Error as e:
    print(f"Database error: {e}")
    if connection:
        connection.rollback()  # Rollback on error
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        

'''
Install connector
↓
Import package
↓
Set config
↓
Connect
↓
Create cursor
↓
Execute SQL
↓
Commit / Rollback
↓
Fetch results
↓
Close cursor
↓
Close connection

'''