"""Optional write example: python registration_demo.py
Creates Noah's DB101 enrolment once. It updates data/enrolments.json.
This is a command-line use case, not an HTTP POST endpoint.
"""
from domain import Student, Course
from storage import load_records, save_records


def register(student_id: int, course_id: str):
    # 1. Resolve both references. A JSON number/string alone is not a link check.
    student_record = None
    for row in load_records("students.json"):
        if row["student_id"] == student_id:
            student_record = row
    course_record = None
    for row in load_records("courses.json"):
        if row["course_id"] == course_id:
            course_record = row
    if student_record is None or course_record is None:
        raise ValueError("Student and course must exist")

    # 2. One enrolment per student/course pair, as in the classroom scenario.
    enrolments = load_records("enrolments.json")
    for row in enrolments:
        if row["student_id"] == student_id and row["course_id"] == course_id:
            raise ValueError("Student is already enrolled in this course")

    # 3. Call the modelled operation, then persist its result.
    student = Student(student_id, student_record["name"])
    course = Course(course_id, course_record["title"])
    record = student.enrol(course).to_record()
    enrolments.append(record)
    save_records("enrolments.json", enrolments)
    return record


if __name__ == "__main__":
    try:
        print(register(1002, "DB101"))
    except ValueError as error:
        print(f"No change: {error}")
