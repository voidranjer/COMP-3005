from sqlalchemy.orm import Session
from Student import Student

class StudentUtils:
    def __init__(self, session: Session):
        self.session = session

    def getAllStudents(self):
        return self.session.query(Student).all()
    
    def addStudent(self, first_name: str, last_name: str, email: str, enrollment_date: str):
        student = Student(first_name, last_name, email, enrollment_date)
        self.session.add(student)
        self.session.commit()

    def updateStudentEmail(self, student_id: int, new_email: str):
        student = self.session.query(Student).filter(Student.student_id == student_id).first()
        student.email = new_email
        self.session.commit()

    def deleteStudent(self, student_id: int):
        student = self.session.query(Student).filter(Student.student_id == student_id).first()
        self.session.delete(student)
        self.session.commit()

    def printAllStudents(self):
        students = self.getAllStudents()
        for student in students:
            print(f"[{student.student_id}] {student.first_name} {student.last_name} - {student.email} (Enrolled on {student.enrollment_date})")

    def closeSession(self):
        self.session.close()