from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship
from .db import Base


class Student(Base):
    __tablename__ = "Students"

    student_id = Column(Integer, primary_key=True)
    name = Column(String)
    enrollment_date = Column(Date)
    grade_relation = relationship("Grade", back_populates='student_relation')
    enrollment_relation = relationship("Enrollment", back_populates='student_relation')
