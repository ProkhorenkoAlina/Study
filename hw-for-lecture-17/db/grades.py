from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base


class Grade(Base):
    __tablename__ = "Grades"

    grade_id = Column(Integer, primary_key=True)
    grade = Column(Integer)
    class_id = Column(Integer, ForeignKey('Classes.class_id'))
    student_id = Column(Integer, ForeignKey('Students.student_id'))

    classes_relation = relationship("Class", back_populates="grade_relation")
    student_relation = relationship("Student", back_populates="grade_relation")
