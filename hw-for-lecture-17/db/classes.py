from sqlalchemy import Column, String, Integer, Time, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base


class Class(Base):
    __tablename__ = "Classes"

    class_id = Column(Integer, primary_key=True)
    name = Column(String)
    time = Column(Time)
    teacher_id = Column(Integer, ForeignKey("Teachers.teacher_id"))
    subject_id = Column(Integer, ForeignKey("Subjects.subject_id"))

    teacher_relation = relationship("Teacher", back_populates="classes_relation")
    subject_relation = relationship("Subject", back_populates="classes_relation")
    grade_relation = relationship("Grade", back_populates="classes_relation")
    enrollment_relation = relationship("Enrollment", back_populates="classes_relation")
    classroom_relation = relationship("Classroom", back_populates="classes_relation")
