
# Create class Student with attributes listed
class Student:
    name = 'No Name Provided'
    address = ''
    age = 0
    GPA = 0
    

# Create a child class of Students who are also Employees
class Employee(Student):
# They receive the same attributes as Students listed above
# but also include these added attributes
    base_pay = 30.00
    job_title = ''
    department = 'General'
    course_discount = 50  # They receive 50% off the course they attend
    

# Create another child class of Students who attend full-time
class FullTime(Student):
# They have all the attributes as Students listed above
# but also include these added attributes
    course_load = 0
    course_list = ''
    anticipated_grad = 'January 2022'
