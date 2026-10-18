"""Run: python objects_demo.py. No file is changed by this example."""
import json
from domain import Student, Course
from storage import load_records


def main():
    student_record = next(row for row in load_records("students.json")
                          if row["student_id"] == 1002)
    course_record = next(row for row in load_records("courses.json")
                         if row["course_id"] == "DB101")
    # Constructor calls create objects from the data we read.
    student = Student(student_record["student_id"], student_record["name"])
    course = Course(course_record["course_id"], course_record["title"])
    enrolment = student.enrol(course)  # The operation shown in our UML class.
    print(f"{student.name} -> {course.title}")
    print(json.dumps(enrolment.to_record(), indent=2))
    print("Object created in memory; nothing saved. No duplicate check in this demo.")


if __name__ == "__main__":
    main()
