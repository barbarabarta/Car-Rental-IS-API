# 4. From UML classes to objects and JSON

[← Trace a request](03-trace-a-request.md) · [Next: change and adapt →](05-change-and-adapt.md)

The modelling class showed `Student.enrol(course)` and the relationship through Enrolment. Open `domain.py`, then run in a second terminal in the repository root:

```sh
python objects_demo.py
```

This creates Noah and the DB101 course as Python objects, calls the modelled operation and prints an enrolment record. It does **not** save or check whether that enrolment already exists.

```python
student = Student(1002, "Noah")
course = Course("DB101", "Databases")
enrolment = student.enrol(course)
record = enrolment.to_record()
```

| Representation | Example / responsibility |
| --- | --- |
| UML class | `Student` with `student_id`, `name`, and `enrol(course)` |
| Python class | `class Student` defines how its objects are constructed and behave |
| Object | `student` refers to one instance with ID 1002 |
| Method call | `student.enrol(course)` creates an Enrolment linking the two IDs |
| Dictionary | `to_record()` returns data that can be encoded as JSON |
| JSON text | `{"student_id": 1002, "course_id": "DB101", "grade": null}` |

`__init__` sets up an instance; `self` is that instance. `None` in Python becomes `null` in JSON. A JSON object has data members, but it is not automatically an instance of our `Student` class and does not contain its executable methods. Python type hints document expected types; ordinary class constructors here do not enforce them automatically.

**Follow the responsibility:** `Student.enrol()` constructs the relationship in memory. Looking up known IDs, preventing duplicate registration and saving the result are additional responsibilities. The [optional registration example](../registration_demo.py) coordinates those steps. The read handlers in `main.py` still return dictionaries directly; they do not call these classes behind the scenes.

**Explain before editing:** Which line corresponds to the UML operation? Why is `grade` initially `None`? Where would you check that a student is not enrolled twice? Would changing a Python object automatically change the JSON file?

`objects_demo.py` uses `next(...)` to obtain a matching record from the supplied data. Its shortened lookup assumes these known records exist; the registration example uses explicit checks. See the [Python guide](python-reading-guide.md#looking-up-a-known-example) if the expression is unfamiliar.

Reference: [Python classes and instances](https://docs.python.org/3.14/tutorial/classes.html).

[← Trace a request](03-trace-a-request.md) · [Next: change and adapt →](05-change-and-adapt.md)
