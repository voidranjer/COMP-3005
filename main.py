from base import Session
from utils import StudentUtils

def main():
    # initialize the session
    session = Session()
    studentUtils = StudentUtils(session)

    # get all students
    students = studentUtils.getAllStudents()
    for student in students:
        print(f"[{student.student_id}] {student.first_name} {student.last_name} - {student.email} (Enrolled on {student.enrollment_date})")
    input("\nPress Enter to continue...")

    # add a student
    print("Adding a new student...")
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    email = input("Enter the email: ")
    enrollment_date = input("Enter the enrollment date (YYYY-MM-DD): ")
    # studentUtils.addStudent("James", "Yap", "contact@jamesyap.org", "2024-03-17")
    studentUtils.addStudent(first_name, last_name, email, enrollment_date)
    studentUtils.printAllStudents()
    print("Added a student!")
    input("\nPress Enter to continue...")


    # update a student's email
    student_id = input("Enter the student ID to update: ")
    new_email = input("Enter the new email: ")
    # studentUtils.updateStudentEmail(student_id, "jamesyap@cmail.carleton.ca")
    studentUtils.updateStudentEmail(student_id, new_email)
    studentUtils.printAllStudents()
    print("Updated a student's email!")
    input("\nPress Enter to continue...")

    # delete a student
    student_id = input("Enter the student ID to delete: ")
    studentUtils.deleteStudent(student_id)
    studentUtils.printAllStudents()
    print("Deleted a student!")
    input("\nPress Enter to continue...")

    studentUtils.closeSession()
    print("Session closed!")

if __name__ == "__main__":
    main()