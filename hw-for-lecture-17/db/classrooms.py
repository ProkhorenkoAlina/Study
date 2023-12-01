from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base


class Classroom(Base):
    __tablename__ = "Classrooms"

    classroom_id = Column(Integer, primary_key=True)
    number = Column(Integer)
    capacity = Column(Integer)
    class_id = Column(Integer, ForeignKey('Classes.class_id'))
    classes_relation = relationship("Class", back_populates="classroom_relation")
