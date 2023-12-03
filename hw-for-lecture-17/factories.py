from datetime import datetime
import factory
import factory.fuzzy
from db import Student, Teacher, Subject, Class, Classroom, Grade, Enrollment, Session


current_session = Session()


class StudentsFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Student
        sqlalchemy_session = current_session
        sqlalchemy_session_persistence = "commit"

    name = factory.Faker("name")
    enrollment_date = factory.fuzzy.FuzzyDate(
        datetime(year=2020, month=10, day=10),
        datetime(year=2022, month=10, day=10),
    )


class TeacherFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Teacher
        sqlalchemy_session = current_session
        sqlalchemy_session_persistence = "commit"

    teacher_id = factory.Sequence(lambda n: n)
    name = factory.Faker("name")
    hire_date = factory.fuzzy.FuzzyDate(
        datetime(year=2020, month=10, day=10),
        datetime(year=2022, month=10, day=10),
    )


class SubjectFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Subject
        sqlalchemy_session = current_session
        sqlalchemy_session_persistence = "commit"

    subject_id = factory.Sequence(lambda n: n)
    subject_name = factory.fuzzy.FuzzyChoice(["English", "Math", "Law"])


class ClassFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Class
        sqlalchemy_session = current_session
        sqlalchemy_session_persistence = "commit"

    name = factory.Sequence(lambda n: f"class {n}")
    time = factory.Sequence(lambda n: f"{n % 24:02d}:00:00")
    teacher_relation = factory.SubFactory(TeacherFactory)
    subject_relation = factory.SubFactory(SubjectFactory)


class GradeFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Grade
        sqlalchemy_session = current_session
        sqlalchemy_session_persistence = "commit"

    grade = factory.Sequence(lambda n: n)
    student_relation = factory.SubFactory(StudentsFactory)
    classes_relation = factory.SubFactory(ClassFactory)


class EnrollmentFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Enrollment
        sqlalchemy_session = current_session
        sqlalchemy_session_persistence = "commit"

    status = factory.fuzzy.FuzzyChoice([True, False])
    student_relation = factory.SubFactory(StudentsFactory)
    classes_relation = factory.SubFactory(ClassFactory)


class ClassroomFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Classroom
        sqlalchemy_session = current_session
        sqlalchemy_session_persistence = "commit"

    number = factory.Sequence(lambda n: n + 1)
    capacity = factory.Sequence(lambda n: n + 20)
    classes_relation = factory.SubFactory(ClassFactory)
