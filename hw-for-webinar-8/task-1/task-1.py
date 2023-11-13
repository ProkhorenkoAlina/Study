class Student:
    def __init__(self, name: str, course_name: str) -> None:
        self.name = name
        self.course_name = course_name
        self.enrolled_courses = set()

    def enroll(self, course: "Course"):
        if course not in self.enrolled_courses:
            self.enrolled_courses.add(course)

    def drop_course(self, course: "Course"):
        self.enrolled_courses.remove(course)

    def view_courses(self) -> str:
        return ", ".join(
            sorted(course.domain for course in self.enrolled_courses)
        )


class Course:
    def __init__(self, domain: str, course_name: str) -> None:
        self.domain = domain
        self.course_name = course_name


class University:
    def __init__(self, name: str) -> None:
        self.name = name
        self.cources = set()
        self.students = set()

    def add_course(self, course: Course) -> None:
        self.cources.add(course)

    def add_student(self, student: Student) -> None:
        self.students.add(student)

    def view_students(self):
        return ", ".join(sorted(student.name for student in self.students))

    def view_courses(self):
        return ", ".join(sorted(course.domain for course in self.cources))


if __name__ == "__main__":
    uni = University("Harvard")

    maths = Course("Mathematics", "MATH101")
    physics = Course("Physics", "PHYS101")

    uni.add_course(maths)
    uni.add_course(physics)

    alice = Student("Alice", "S101")

    uni.add_student(alice)

    alice.enroll(maths)

    assert alice.view_courses() == "Mathematics"

    assert uni.view_students() == "Alice"
    assert uni.view_courses() == "Mathematics, Physics"

    alice.drop_course(maths)

    assert alice.view_courses() == ""
