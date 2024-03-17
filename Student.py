from sqlalchemy import Column, Text, Integer, Date

from base import Base


class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(Text, nullable=False)
    last_name = Column(Text, nullable=False)
    email = Column(Text, nullable=False, unique=True)
    enrollment_date = Column(Date)

    def __init__(self, first_name, last_name, email, enrollment_date):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.enrollment_date = enrollment_date