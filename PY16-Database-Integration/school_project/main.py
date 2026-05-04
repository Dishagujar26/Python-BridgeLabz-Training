from course_operations import *
from student_operations import *

# Create tables
create_courses_table()
create_students_table()

# Insert courses
add_course("Python Programming", 3, "Dr. Smith")
add_course("Java Programming", 4, "Prof. Sharma")

# Insert students
add_student("Disha", "disha@gmail.com", 1)
add_student("Rahul", "rahul@gmail.com", 2)

# Read courses
print("Courses:")
get_all_courses()

# Read students with course details
print("Students:")
get_all_students()

# Update course
update_course_instructor(1, "Dr. Mehta")

# Update student
update_student_email(1, "disha_new@gmail.com")

# Delete student
delete_student(2)

# Delete course
# delete_course(2)