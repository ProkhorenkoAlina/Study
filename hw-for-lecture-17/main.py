from factories import EnrollmentFactory, current_session
from db import Student, Enrollment, Class, Subject


if __name__ == "__main__":
    EnrollmentFactory.create_batch(100)

    english_students = current_session.query(
        Student, Enrollment, Class, Subject
    ).filter(
        Student.student_id == Enrollment.student_id
    ).filter(
        Enrollment.class_id == Class.class_id
    ).filter(
        Subject.subject_id == Class.subject_id
    ).filter(
        Subject.subject_name == "English"
    ).all()

    for student_info in english_students:
        student, enrollment, class_, subject = student_info
        print(student.student_id, student.name, subject.subject_name)
