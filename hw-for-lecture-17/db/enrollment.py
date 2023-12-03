from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base


class Enrollment(Base):
    __tablename__ = "Enrollments"

    enrollment_id = Column(Integer, primary_key=True)
    status = Column(Boolean)
    class_id = Column(Integer, ForeignKey('Classes.class_id'))
    student_id = Column(Integer, ForeignKey('Students.student_id'))
    classes_relation = relationship("Class", back_populates="enrollment_relation")
    student_relation = relationship("Student", back_populates="enrollment_relation")

