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
    studentUtils.addStudent("James", "Yap", "contact@jamesyap.org", "2024-03-17")
    studentUtils.printAllStudents()
    print("Added a student!")
    input("\nPress Enter to continue...")

    student_id = input("Enter the student ID to update: ")

    # update a student's email
    studentUtils.updateStudentEmail(student_id, "jamesyap@cmail.carleton.ca")
    studentUtils.printAllStudents()
    print("Updated a student's email!")
    input("\nPress Enter to continue...")

    # delete a student
    studentUtils.deleteStudent(student_id)
    studentUtils.printAllStudents()
    print("Deleted a student!")
    input("\nPress Enter to continue...")

    studentUtils.closeSession()
    print("Session closed!")

if __name__ == "__main__":
    main()