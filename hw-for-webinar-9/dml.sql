INSERT INTO "Students" ("name", "enrollment_date") VALUES
('John Doe', '2023-01-01'),
('Jane Smith', '2023-01-02'),
('Bob Johnson', '2023-01-03'),
('Alice Williams', '2023-01-04'),
('Charlie Brown', '2023-01-05');

INSERT INTO "Teachers" ("name", "hired_date") VALUES
('Mr. Anderson', '2023-01-01'),
('Mrs. Davis', '2023-01-02'),
('Dr. Wilson', '2023-01-03'),
('Ms. Thompson', '2023-01-04'),
('Prof. White', '2023-01-05');

INSERT INTO "Subjects" ("subject_name") VALUES
('Mathematics'),
('Science'),
('History'),
('English'),
('Computer Science');

INSERT INTO "Classes" ("teacher_id", "subject_id", "name", "time") VALUES
(1, 1, 'Math Class A', '08:00:00'),
(2, 2, 'Science Class B', '09:30:00'),
(3, 3, 'History Class C', '11:00:00'),
(4, 4, 'English Class D', '13:00:00'),
(5, 5, 'Computer Science Class E', '14:30:00');

INSERT INTO "Classrooms" ("class_id", "number", "capacity") VALUES
(1, 101, 30),
(2, 102, 25),
(3, 103, 35),
(4, 104, 40),
(5, 105, 20);

INSERT INTO "Grades" ("student_id", "class_id", "grade") VALUES
(1, 1, 90),
(2, 1, 85),
(3, 2, 92),
(4, 2, 88),
(5, 3, 95);

INSERT INTO "Enrollment" ("student_id", "class_id", "status") VALUES
(1, 1, true),
(2, 1, true),
(3, 2, true),
(4, 2, true),
(5, 3, true);