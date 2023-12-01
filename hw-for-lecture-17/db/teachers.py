from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship
from .db import Base


class Teacher(Base):
    __tablename__ = "Teachers"

    teacher_id = Column(Integer, primary_key=True)
    name = Column(String)
    hire_date = Column(Date)

    classes_relation = relationship("Class", back_populates='teacher_relation')
