from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from .db import Base


class Subject(Base):
    __tablename__ = "Subjects"

    subject_id = Column(Integer, primary_key=True)
    subject_name = Column(String)

    classes_relation = relationship("Class", back_populates="subject_relation")
