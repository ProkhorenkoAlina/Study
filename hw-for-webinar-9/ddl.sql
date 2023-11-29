CREATE TABLE "Students" (
	"student_id" serial NOT NULL,
	"name" varchar(50) NOT NULL,
	"enrollment_date" DATE NOT NULL,
	CONSTRAINT "Students_pk" PRIMARY KEY ("student_id")
);

CREATE TABLE "Teachers" (
	"teacher_id" serial NOT NULL,
	"name" varchar(50) NOT NULL,
	"hired_date" DATE NOT NULL,
	CONSTRAINT "Teachers_pk" PRIMARY KEY ("teacher_id")
);

CREATE TABLE "Subjects" (
	"subject_id" serial NOT NULL,
	"subject_name" varchar(50) NOT NULL,
	CONSTRAINT "Subjects_pk" PRIMARY KEY ("subject_id")
);

CREATE TABLE "Classes" (
	"class_id" serial NOT NULL,
	"teacher_id" integer NOT NULL,
	"subject_id" integer NOT NULL,
	"name" varchar(50) NOT NULL,
	"time" TIME NOT NULL,
	CONSTRAINT "Classes_pk" PRIMARY KEY ("class_id")
);

CREATE TABLE "Classrooms" (
	"classroom_id" serial NOT NULL,
	"class_id" integer NOT NULL,
	"number" integer NOT NULL,
	"capacity" integer NOT NULL,
	CONSTRAINT "Classrooms_pk" PRIMARY KEY ("classroom_id")
);

CREATE TABLE "Grades" (
	"grade_id" serial NOT NULL,
	"student_id" integer NOT NULL,
	"class_id" integer NOT NULL,
	"grade" integer NOT NULL,
	CONSTRAINT "Grades_pk" PRIMARY KEY ("grade_id")
);

CREATE TABLE "Enrollment" (
	"entollment_id" serial NOT NULL,
	"student_id" integer NOT NULL,
	"class_id" integer NOT NULL,
	"status" BOOLEAN NOT NULL,
	CONSTRAINT "Enrollment_pk" PRIMARY KEY ("entollment_id")
);


ALTER TABLE "Classes" ADD CONSTRAINT "Classes_fk0" FOREIGN KEY ("teacher_id") REFERENCES "Teachers"("teacher_id");
ALTER TABLE "Classes" ADD CONSTRAINT "Classes_fk1" FOREIGN KEY ("subject_id") REFERENCES "Subjects"("subject_id");

ALTER TABLE "Classrooms" ADD CONSTRAINT "Classrooms_fk0" FOREIGN KEY ("class_id") REFERENCES "Classes"("class_id");

ALTER TABLE "Grades" ADD CONSTRAINT "Grades_fk0" FOREIGN KEY ("student_id") REFERENCES "Students"("student_id");
ALTER TABLE "Grades" ADD CONSTRAINT "Grades_fk1" FOREIGN KEY ("class_id") REFERENCES "Classes"("class_id");

ALTER TABLE "Enrollment" ADD CONSTRAINT "Enrollment_fk0" FOREIGN KEY ("student_id") REFERENCES "Students"("student_id");
ALTER TABLE "Enrollment" ADD CONSTRAINT "Enrollment_fk1" FOREIGN KEY ("class_id") REFERENCES "Classes"("class_id");