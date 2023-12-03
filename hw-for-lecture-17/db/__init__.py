from .students import Student
from .teachers import Teacher
from .subjects import Subject
from .classes import Class
from .classrooms import Classroom
from .grades import Grade
from .enrollment import Enrollment
from .db import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://admin:password@db/study_managment")

Base.metadata.create_all(engine)
conn = engine.connect()

Session = sessionmaker(bind=engine)